import discord
from discord.ext import commands
import os
import asyncio
import itertools
import sys
import traceback
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL

intents = discord.Intents.default()
intents.members = True
intents = intents.all()
client = commands.Bot(command_prefix="?", intents=intents)
client.remove_command("help")

ytdlopts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # ipv6 addresses cause issues sometimes
}

ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}

ytdl = YoutubeDL(ytdlopts)


class VoiceConnectionError(commands.CommandError):
    """Custom Exception class for connection errors."""


class InvalidVoiceChannel(VoiceConnectionError):
    """Exception for cases of invalid Voice Channels."""


class YTDLSource(discord.PCMVolumeTransformer):

    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester

        self.title = data.get('title')
        self.web_url = data.get('webpage_url')

        # YTDL info dicts (data) have other useful information you might want
        # https://github.com/rg3/youtube-dl/blob/master/README.md

    def __getitem__(self, item: str):
        """Allows us to access attributes similar to a dict.
        This is only useful when you are NOT downloading.
        """
        return self.__getattribute__(item)

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False):
        loop = loop or asyncio.get_event_loop()

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        await ctx.send(f'```ini\n[Added {data["title"]} to the Queue.]\n```')

        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

        return cls(discord.FFmpegPCMAudio(source), data=data, requester=ctx.author)

    @classmethod
    async def regather_stream(cls, data, *, loop):
        """Used for preparing a stream, instead of downloading.
        Since Youtube Streaming links expire."""
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']

        to_run = partial(ytdl.extract_info, url=data['webpage_url'], download=False)
        data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(data['url']), data=data, requester=requester)


filtered_words = ['fdp', 'arrombado', 'buceta', 'pinto', 'caralho', 'idiota', 'escroto', 'porra']


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='?help para saber mais'))
    print("Bot online!")
    print(client.user.name)
    print(client.user.id)


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()
            break  # stops it constantly spamming / continues the loop

    if "noob" in msg.content.lower():
        await msg.add_reaction("<:mds:703304861575544962>")
        await msg.add_reaction("<:pikoh:606574166497558538>")
    if "nub" in msg.content.lower():
        await msg.add_reaction("<:mds:703304861575544962>")
        await msg.add_reaction("<:pikoh:606574166497558538>")
    if "formulário" in msg.content.lower():
        await msg.add_reaction("<:desconfiadx:610229151840075786>")
    if "formulario" in msg.content.lower():
        await msg.add_reaction("<:desconfiadx:610229151840075786>")
    if "austin" in msg.content.lower():
        await msg.add_reaction("🇳")
        await msg.add_reaction("🇴")
        await msg.add_reaction("🇧")
    if "pera" in msg.content.lower():
        await msg.add_reaction("🍐")

    await client.process_commands(msg)


@client.event
async def on_message_delete(message):
    if message.author.bot:
        return
    channel = client.get_channel(id=797203131019689994)  # id do canal em que as mensagens serão arquivadas
    await channel.send(f'{message.author} deleted this message:\n{message.content}')


@client.event
async def on_member_join(member):
    channel = client.get_channel(id=782802548212891658)  # verifique aqui

    await channel.send(f'Bem vindo ao servidor oficial dos Helpers BR {member.mention}! Por favor escreva seu nick no '
                       f'jogo utilizando esses caracteres para a tag ﹟ ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ . Não se esqueça de ler as regras em '
                       f'<#515924836724506634> e divirta-se! Para mais comandos digite ?help no canal <#789349633121845249>')


@client.command(aliases=['sobre'])
async def Sobre(ctx):
    await ctx.send('Olá! Eu sou um bot experimental e estou aqui para te ajudar! Fui programado pelo Kanskje e espero '
                   'fazer um bom trabalho!')


@client.command(aliases=['recrutamento'])
async def Recrutamento(ctx):
    await ctx.send('O recrutamento para a equipe dos Helpers BR está aberto! Para saber mais detalhes, entre nesse '
                   'link: https://atelier801.com/topic?f=5&t=886189&p=1 e clique na aba "recrutamento".')


@client.command(aliases=['staff'])
async def Staff(ctx):
    await ctx.send('Lista de toda a Staff >> https://atelier801.com/staff \n'
                   'Tópico de anúncios da Staff BR >> https://atelier801.com/topic?f=5&t=788911&p=1'
                   '\n\nSe quiser algo mais expecífico tente os comandos ?moderação, ?sentinela ou ?mapcrew.')


@client.command(aliases=['moderação', 'moderacao', 'moderaçao', 'moderacão', 'Moderação', 'Moderaçao', 'Moderacão'])
async def Moderacao(ctx):
    await ctx.send('Informações sobre recrutamento >> https://atelier801.com/topic?f=6&t=855148&p=1#m1 \nFeedback '
                   'para a moderação >> https://atelier801.com/topic?f=5&t=927074&p=1 \nCentral de banimentos >> '
                   'https://atelier801.com/topic?f=5&t=814024&p=1')


@client.command(aliases=['sentinela'])
async def Sentinela(ctx):
    await ctx.send('Informações sobre recrutamento >> https://atelier801.com/topic?f=6&t=891854&p=1#m1 \nFeedback '
                   'para os sentinelas >> https://atelier801.com/topic?f=5&t=927060&p=1#m1 ')


@client.command(aliases=['mapcrew'])
async def Mapcrew(ctx):
    await ctx.send('Informações sobre recrutamento >> https://atelier801.com/topic?f=6&t=846172&p=1#m1')


@client.command(aliases=['evento'])
async def Evento(ctx):
    await ctx.send('Para saber mais informações sobre o evento atual no jogo, utilize esse link: '
                   'https://atelier801.com/topic?f=6&t=879878&p=1 \nCaso você queira um tópico com mais discussão e '
                   'mais movimento, pode tentar o tópico em inglês: https://atelier801.com/topic?f=6&t=888989&p=1 ('
                   'não temos ligação com esse tópico).')


@client.command(aliases=['pelo', 'pelos', 'Pelos'])
async def Pelo(ctx):
    await ctx.send('https://atelier801.com/topic?f=6&t=893313&p=1#m1')


@client.command(aliases=['café', 'Café', 'cafe'])
async def Cafe(ctx):
    await ctx.send('Para usar o café é necessário ter 1000 queijos coletados e 30 horas online.')


@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="Help", description="lista com todos os comandos.")

    em.add_field(name="Introdução", value="sobre")
    em.add_field(name="Helpers", value="recrutamento, evento")
    em.add_field(name="Staff", value="staff, moderação, sentinela, mapcrew")
    em.add_field(name="Utilidade", value="pelo, cafe")

    await ctx.send(embed=em)


@client.command()
async def ping(ctx):
    await ctx.send(f'Latencia: {round(client.latency * 1000)}ms')


class MusicPlayer(commands.Cog):
    """A class which is assigned to each guild using the bot for Music.
    This class implements a queue and loop, which allows for different guilds to listen to different playlists
    simultaneously.
    When the bot disconnects from the Voice it's instance will be destroyed.
    """

    __slots__ = ('bot', '_guild', '_channel', '_cog', 'queue', 'next', 'current', 'np', 'volume')

    def __init__(self, ctx):
        self.bot = ctx.bot
        self._guild = ctx.guild
        self._channel = ctx.channel
        self._cog = ctx.cog

        self.queue = asyncio.Queue()
        self.next = asyncio.Event()

        self.np = None  # Now playing message
        self.volume = .5
        self.current = None

        ctx.bot.loop.create_task(self.player_loop())

    async def player_loop(self):
        """Our main player loop."""
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            self.next.clear()

            try:
                # Wait for the next song. If we timeout cancel the player and disconnect...
                async with timeout(300):  # 5 minutes...
                    source = await self.queue.get()
            except asyncio.TimeoutError:
                return self.destroy(self._guild)

            if not isinstance(source, YTDLSource):
                # Source was probably a stream (not downloaded)
                # So we should regather to prevent stream expiration
                try:
                    source = await YTDLSource.regather_stream(source, loop=self.bot.loop)
                except Exception as e:
                    await self._channel.send(f'There was an error processing your song.\n'
                                             f'```css\n[{e}]\n```')
                    continue

            source.volume = self.volume
            self.current = source

            self._guild.voice_client.play(source, after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
            self.np = await self._channel.send(f'**Now Playing:** `{source.title}` requested by '
                                               f'`{source.requester}`')
            await self.next.wait()

            # Make sure the FFmpeg process is cleaned up.
            source.cleanup()
            self.current = None

            try:
                # We are no longer playing this song...
                await self.np.delete()
            except discord.HTTPException:
                pass

    def destroy(self, guild):
        """Disconnect and cleanup the player."""
        return self.bot.loop.create_task(self._cog.cleanup(guild))


class Music(commands.Cog):
    """Music related commands."""

    __slots__ = ('bot', 'players')

    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    async def cleanup(self, guild):
        try:
            await guild.voice_client.disconnect()
        except AttributeError:
            pass

        try:
            del self.players[guild.id]
        except KeyError:
            pass

    async def __local_check(self, ctx):
        """A local check which applies to all commands in this cog."""
        if not ctx.guild:
            raise commands.NoPrivateMessage
        return True

    async def __error(self, ctx, error):
        """A local error handler for all errors arising from commands in this cog."""
        if isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.send('This command can not be used in Private Messages.')
            except discord.HTTPException:
                pass
        elif isinstance(error, InvalidVoiceChannel):
            await ctx.send('Error connecting to Voice Channel. '
                           'Please make sure you are in a valid channel or provide me with one')

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    def get_player(self, ctx):
        """Retrieve the guild player, or generate one."""
        try:
            player = self.players[ctx.guild.id]
        except KeyError:
            player = MusicPlayer(ctx)
            self.players[ctx.guild.id] = player

        return player

    @commands.command(name='connect', aliases=['join'])
    async def connect_(self, ctx):
        try:
            channel = ctx.author.voice.channel
        except AttributeError:
            raise InvalidVoiceChannel('No channel to join.')

        vc = ctx.voice_client

        if vc:
            if vc.channel.id == channel.id:
                return
            try:
                await vc.move_to(channel)
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Moving to channel: <{channel}> timed out.')
        else:
            try:
                await channel.connect()
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Connecting to channel: <{channel}> timed out.')

        await ctx.send(f'Connected to: **{channel}**', )

    @commands.command(name='play', aliases=['sing'])
    async def play_(self, ctx, *, search: str):
        await ctx.trigger_typing()

        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)

        player = self.get_player(ctx)

        # If download is False, source will be a dict which will be used later to regather the stream.
        # If download is True, source will be a discord.FFmpegPCMAudio with a VolumeTransformer.
        source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=False)

        await player.queue.put(source)

    @commands.command(name='pause')
    async def pause_(self, ctx):
        """Pause the currently playing song."""
        vc = ctx.voice_client

        if not vc or not vc.is_playing():
            return await ctx.send('I am not currently playing anything!')
        elif vc.is_paused():
            return

        vc.pause()
        await ctx.send(f'**`{ctx.author}`**: Paused the song!')

    @commands.command(name='resume')
    async def resume_(self, ctx):
        """Resume the currently paused song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('I am not currently playing anything!', )
        elif not vc.is_paused():
            return

        vc.resume()
        await ctx.send(f'**`{ctx.author}`**: Resumed the song!')

    @commands.command(name='skip')
    async def skip_(self, ctx):
        """Skip the song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('I am not currently playing anything!')

        if vc.is_paused():
            pass
        elif not vc.is_playing():
            return

        vc.stop()
        await ctx.send(f'**`{ctx.author}`**: Skipped the song!')

    @commands.command(name='queue', aliases=['q', 'playlist'])
    async def queue_info(self, ctx):
        """Retrieve a basic queue of upcoming songs."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('I am not currently connected to voice!')

        player = self.get_player(ctx)
        if player.queue.empty():
            return await ctx.send('There are currently no more queued songs.')

        # Grab up to 5 entries from the queue...
        upcoming = list(itertools.islice(player.queue._queue, 0, 5))

        fmt = '\n'.join(f'**`{_["title"]}`**' for _ in upcoming)
        embed = discord.Embed(title=f'Upcoming - Next {len(upcoming)}', description=fmt)

        await ctx.send(embed=embed)

    @commands.command(name='now_playing', aliases=['np', 'current', 'currentsong', 'playing'])
    async def now_playing_(self, ctx):
        """Display information about the currently playing song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('I am not currently connected to voice!', )

        player = self.get_player(ctx)
        if not player.current:
            return await ctx.send('I am not currently playing anything!')

        try:
            # Remove our previous now_playing message.
            await player.np.delete()
        except discord.HTTPException:
            pass

        player.np = await ctx.send(f'**Now Playing:** `{vc.source.title}` '
                                   f'requested by `{vc.source.requester}`')

    @commands.command(name='volume', aliases=['vol'])
    async def change_volume(self, ctx, *, vol: float):
        """Change the player volume.
        Parameters
        ------------
        volume: float or int [Required]
            The volume to set the player to in percentage. This must be between 1 and 100.
        """
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('I am not currently connected to voice!', )

        if not 0 < vol < 101:
            return await ctx.send('Please enter a value between 1 and 100.')

        player = self.get_player(ctx)

        if vc.source:
            vc.source.volume = vol / 100

        player.volume = vol / 100
        await ctx.send(f'**`{ctx.author}`**: Set the volume to **{vol}%**')

    @commands.command(name='stop', aliases=['leave'])
    async def stop_(self, ctx):
        """Stop the currently playing song and destroy the player.
        !Warning!
            This will destroy the player assigned to your guild, also deleting any queued songs and settings.
        """
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('I am not currently playing anything!')

        await self.cleanup(ctx.guild)


@client.command(aliases=['Clear', 'clear', 'purge', 'Purge'])
@commands.has_role("Helpers")
async def clear_messages(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Foram apagadas {amount} mensagens.')


@client.event
async def on_command_error(ctx, error):
    embed = discord.Embed(
    title='',
    color=discord.Color.red())
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.MissingPermissions):
        embed.add_field(name=f'Invalid Permissions', value=f'You dont have {error.missing_perms} permissions.')
        await ctx.send(embed=embed)
    else:
        embed.add_field(name = f':x: Terminal Error', value = f"```{error}```")
        await ctx.send(embed = embed)
        raise error


client.run(os.environ['token'])
