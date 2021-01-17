import discord
from discord.ext import commands
import os
import asyncio
import random

intents = discord.Intents.default()
intents.members = True
intents = intents.all()
client = commands.Bot(command_prefix="?", intents=intents)
client.remove_command("help")

filtered_words = ['puta', 'arrombado', 'buceta', 'pinto', 'caralho', 'idiota', 'escroto', 'porra']


@client.event
async def on_ready():
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
            break  ## stops it constantly spamming / continues the loop

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


@client.command(aliases=['moderação', 'moderacao', 'moderaçao', 'moderacão', 'Moderacao', 'Moderaçao', 'Moderacão'])
async def Moderação(ctx):
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


# @help.command()
# async def sobre(ctx):
# em = discord.Embed(title='Sobre', description='Uma pequena descrição sobre o bot.')
# await ctx.send(embed=em)


def convert(time):
    pos = ['s', 'm', 'h', 'd']
    time_dict = {'s': 1, 'm': 60, 'h': 3600, 'd': 3600 * 24}
    unit = time[-1]
    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


@client.command()
@commands.has_role("Helpers")
async def sorteio(ctx):
    global winner
    await ctx.send("Inicio do sorteio. Responda as seguintes perguntas em até 30 segundos.")
    questions = ['Em qual canal o sorteio deve ser realizado?', 'Qual a duração do sorteio? (s|m|h|d)',
                 'O que vai ser sorteado?', 'Quantas pessoas serão sorteadas?']

    answers = []
    role = discord.utils.get(ctx.guild.roles, name="Sorteios")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Você demorou demais para responder. Tente novamente.")
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"Você não mencionou um canal. Tente {ctx.channel.mention} da próxima vez.")
        return

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send("Você não usou uma unidade de tempo correta (s|m|h|d). Tente novamente.")
        return
    elif time == -2:
        await ctx.send("Você não usou um número inteiro para a hora. Tente novamente.")
        return

    prize = answers[2]

    ganhadores = int(answers[3])
    if ganhadores == -1:
        await ctx.send("Numero de ganhadores inválido.")
        return

    await ctx.send(f"O sorteio será no canal {channel.mention} com duração de {answers[1]} e terá {answers[3]} ganhador(es).")

    embed = discord.Embed(title="Sorteio!", description=f"{prize}")
    embed.add_field(name="Feito por:", value=ctx.author.mention)
    embed.set_footer(text=f'Termina em {answers[1]}')

    my_msg = await channel.send(embed=embed)

    await my_msg.add_reaction("<:derp:703304861512499271>")
    await channel.send(f"{role.mention}")
    await asyncio.sleep(time)

    new_message = await channel.fetch_message(my_msg.id)

    users = await new_message.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    for i in range(answers[3]):
        winner = random.choice(users)

    await channel.send(f"Parabéns {winner.mention}! Você ganhou {prize}!")


@client.command()
@commands.has_role("Helpers")
async def refazer(ctx, channel: discord.TextChannel, id_: int):
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await ctx.send("O id foi enviado de maneira incorreta.")
        return

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Parabéns {winner.mention}, você é o novo vencedor!")


'''time_regex = re.compile(r"(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}


def convert(argument):
    args = argument.lower()
    matches = re.findall(time_regex, args)
    time = 0
    for key, value in matches:
        try:
            time += time_dict[value] * float(key)
        except KeyError:
            raise commands.BadArgument(
                f"{value} is an invalid time key! h|m|s|d are valid arguments"
            )
        except ValueError:
            raise commands.BadArgument(f"{key} is not a number!")
    return round(time)


@client.command()
@commands.has_role('Helpers')
async def start(ctx, timing, winners: int, *, prize):
    await ctx.send('Começando o sorteio!', delete_after=3)
    gwembed = discord.Embed(
        title="🎉 __**Sorteio**__ 🎉",
        description=f'O que está sendo sorteado: {prize}',
        color=0xb4e0fc
    )
    time = convert(timing)
    gwembed.set_footer(text=f"Esse sorteio acaba {time} segundos após essa mensagem.")
    gwembed = await ctx.send(embed=gwembed)
    await gwembed.add_reaction("<:derp:703304861512499271>")
    await asyncio.sleep(time)
    message = await ctx.fetch_message(gwembed.id)
    users = await message.reactions[0].users().flatten()
    users.pop(users.index(ctx.guild.me))
    if len(users) == 0:
        await ctx.send("Não houve ganhadores.")
        return
    for i in range(winners):
        winner = random.choice(users)
        await ctx.send(f"**Parabéns {winner}!**")'''


@client.command(aliases=['Clear', 'clear', 'purge', 'Purge'])
@commands.has_role("Helpers")
async def clear_messages(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Foram apagadas {amount} mensagens.')


client.run(os.environ['token'])
