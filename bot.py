import asyncio
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents = intents.all()
client = commands.Bot(command_prefix="?", intents=intents)
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='?help para saber mais'))
    channel = client.get_channel(id=797141089998864465)
    await channel.send(f'O melhor bot do server chegou! <@283650918749044736>')
    print("Bot online!")
    print(client.user.name)
    print(client.user.id)


@client.event
async def on_message(msg):
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
        if msg.author == client.user:
            return
        else:
            await msg.add_reaction("🇳")
            await msg.add_reaction("🇴")
            await msg.add_reaction("🇧")
    if "pera" in msg.content.lower():
        await msg.add_reaction("🍐")

    await client.process_commands(msg)


@client.event
async def on_message(msg):
    if "kaldt" in msg.content.lower():
        if msg.author == client.user:
            return
        else:
            await msg.channel.send("O que estão falando sobre mim? 👀")

    if "austin" in msg.content.lower():
        if msg.author == client.user:
            return
        else:
            await msg.channel.send("Austin? O maior noob que ja vi")

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

    await channel.send(f'Bem vindo ao servidor oficial dos Helpers BR {member.mention}! Primeiro de tudo, certifique-se'
                       f' que sua conta está verificada no servidor oficial do Transformice. Caso não esteja, digite '
                       f'?verify para ver o passo a passo. Caso precise do link do servidor, digite ?tfm. Em seguida, '
                       f'leia o canal <#515924836724506634>. e por fim escreva seu nickname no jogo utilizando esses'
                       f' caracteres para a tag ﹟ ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ . Para mais comandos digite ?help no canal '
                       f'<#789349633121845249>')


@client.command(aliasssses=['Tfm'])
async def tfm(ctx):
    await ctx.send("discord.gg/transformice")


@client.command(aliasses=['verificar', 'verificação', 'Verify', 'Verificar', 'Verificação'])
async def verify(ctx):
    await ctx.send('Para verificar a sua conta no servidor oficial do Transformice, acesse o link '
                   'https://staff.atelier801.com/discord \nEm seguida, escolha a bandeira da sua comunidade e faça '
                   'login na sua conta do discord, caso necessário. Em seguida, digite o seu nick do Transformice e '
                   'substitua a tag #0000 caso necessário. Por fim, verifique a sua caixa de entrada do fórum e '
                   'clique na URL que lhe foi enviado.')


@client.command(aliases=['sobre'])
async def Sobre(ctx):
    await ctx.send('Olá! Eu sou um bot experimental e estou aqui para te ajudar! Fui programado pelo Kanskje e espero '
                   'fazer um bom trabalho! Se tiver sugestões pode pingar o meu criador ou mandar uma mensagem privada!')


@client.command(aliases=['recrutamento'])
async def Recrutamento(ctx):
    await ctx.send('O recrutamento para a equipe dos Helpers BR está aberto! Para saber mais detalhes, entre nesse '
                   'link: https://atelier801.com/topic?f=5&t=886189&p=1 e clique na aba "recrutamento".')


@client.command(aliases=['staff'])
async def Staff(ctx):
    await ctx.send('Lista de toda a Staff >> https://atelier801.com/staff \n'
                   'Tópico de anúncios da Staff BR >> https://atelier801.com/topic?f=5&t=788911&p=1'
                   '\n\nSe quiser algo mais expecífico tente os comandos ?moderação, ?sentinela ou ?mapcrew.')


@client.command(
    aliases=['moderação', 'moderacao', 'moderaçao', 'moderacão', 'Moderação', 'Moderaçao', 'Moderacão', 'mod', 'Mod'])
async def Moderacao(ctx):
    await ctx.send('Informações sobre recrutamento >> https://atelier801.com/topic?f=6&t=855148&p=1#m1 \nFeedback '
                   'para a moderação >> https://atelier801.com/topic?f=5&t=927074&p=1 \nCentral de banimentos >> '
                   'https://atelier801.com/topic?f=5&t=814024&p=1')


@client.command(aliases=['sentinela', 'Sentinelas', 'sentinelas'])
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
                   'mais movimento, pode tentar o tópico em inglês: https://atelier801.com/topic?f=6&t=894075&p=1 ('
                   'não temos ligação com esse tópico).')


@client.command(aliases=['pelo', 'pelos', 'Pelos'])
async def Pelo(ctx):
    await ctx.send('https://atelier801.com/topic?f=6&t=893313&p=1#m1')


@client.command(aliases=['café', 'Café', 'cafe'])
async def Cafe(ctx):
    await ctx.send('Para usar o café é necessário ter 1000 queijos coletados e 30 horas online.')


@client.group(invoke_without_command=True)
async def help(ctx):
    await ctx.send(f"Os comandos deste bot são: \n\n"
                   f"🔸 **?Sobre** --> Uma pequena introdução sobre o bot.\n"
                   f"🔸 **?Recrutamento** --> Link para o recrutamento dos Helpers BR.\n"
                   f"🔸 **?Staff** --> Links úteis sobre a staff em geral.\n"
                   f"🔸 **?Moderação** --> Links úteis sobre a moderação.\n"
                   f"🔸 **?Sentinela** --> Links úteis sobre os sentinelas.\n"
                   f"🔸 **?Mapcrew** --> Links úteis sobre os mapcrews.\n"
                   f"🔸 **?Evento** --> Links sobre o evento atual no jogo.\n"
                   f"🔸 **?Pelo** --> Link para ver o cóigo das cores dos pelos.\n"
                   f"🔸 **?Café** --> Requisitos para poder falar no café.\n"
                   f"🔸 **?Say** --> Faz o bot falar qualquer coisa.\n"
                   f"🔸 **?Ping** --> Mostra o ping do bot.\n"
                   f"🔸 **?Tfm** --> Mostra o link para o servidor oficial do Transformice no discord.\n"
                   f"🔸 **?Verify** --> Mostra um pequeno tutorial de como verificar a conta no servidor oficial do Transformice.\n")


@client.command()
async def ping(ctx):
    await ctx.send(f'Latencia: {round(client.latency * 1000)}ms')


@client.command(aliases=['Clear', 'clear', 'purge', 'Purge'])
@commands.has_role("Helpers")
async def clear_messages(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{ctx.message.author.mention} apagou {amount} mensagens.')


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
        embed.add_field(name=f':x: Terminal Error', value=f"```{error}```")
        await ctx.send(embed=embed)
        raise error


@client.command(aliasses=['Mes', 'mês', 'Mês'])
@commands.has_role("Helpers")
async def mes(msg):
    my_message = await msg.send("Em quem você quer votar para Helper do Mês desse mês?\n\n"
                                "🇦 Amanda\n"
                                "🇧 Austinbacky\n"
                                "🇨 Backyardigans\n"
                                "🇩 Henry\n"
                                "🇪 Jean\n"
                                "🇫 Kanskje\n"
                                "🇬 Kigglybuff\n"
                                "🇭 Mouz\n"
                                "🇮 Provincias\n"
                                "🇯 Santoex\n"
                                "🇰 Sorreltail\n"
                                "🇱 Tiradez\n"
                                "🇲 Vlump\n"
                                "🇳 Xlivrox\n"
                                "🇴 Yukari")
    await my_message.add_reaction("🇦")
    await my_message.add_reaction("🇧")
    await my_message.add_reaction("🇨")
    await my_message.add_reaction("🇩")
    await my_message.add_reaction("🇪")
    await my_message.add_reaction("🇫")
    await my_message.add_reaction("🇬")
    await my_message.add_reaction("🇭")
    await my_message.add_reaction("🇮")
    await my_message.add_reaction("🇯")
    await my_message.add_reaction("🇰")
    await my_message.add_reaction("🇱")
    await my_message.add_reaction("🇲")
    await my_message.add_reaction("🇳")
    await my_message.add_reaction("🇴")


@client.command(pass_context=True)
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(f"{message}")


##emojis = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹','🇺', '🇻', '🇼', '🇽', '🇾', '🇿']


'''@client.command(aliasses=['r'])
async def restart(ctx):
    if ctx.author.id != 283650918749044736:
        return
    await ctx.send("Bot reiniciando...")
    await client.logout()
    await client.login("token", bot=True)
    channel = client.get_channel(id=797141089998864465)
    await channel.send("Bot reiniciado!")'''


@client.command()
async def restart(ctx):
    channel = client.get_channel(id=797141089998864465)
    await channel.sned("Bot reiniciando...")
    await client.close()

client.run(os.environ['token'])
