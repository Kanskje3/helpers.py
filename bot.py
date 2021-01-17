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


@client.command(aliases=['poll', 'votaçao', 'votacao', 'votacão', 'Poll'])
async def votação(ctx, question, *options: str):
    if len(options) <= 1:
        await ctx.send('Você precisa de mais opções para fazer uma votação.')
        return
    if len(options) > 26:
        await ctx.send('Você não poed fazer uma votação com mais de 26 itens.')
        return

    if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
        ctx.add_reactions(['✅'])
        ctx.add_reactions(['❌'])
    else:
        reactions = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹',
                     '🇺', '🇻', '🇼', '🇽', '🇾', '🇿']

    description = []
    for x, option in enumerate(options):
        description += '\n {} {}'.format(reactions[x], option)
    embed = discord.Embed(title=question, description=''.join(description))
    react_message = await ctx.send(embed=embed)
    for reaction in reactions[:len(options)]:
        await react_message.edit(react_message, reaction)
    embed.set_footer(text='Poll ID: {}'.format(react_message.id))
    await react_message.edit(embed=embed)


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
    await ctx.send("Inicio do sorteio. Responda as seguintes perguntas em até 30 segundos.")
    questions = ['Em qual canal o sorteio deve ser realizado?', 'Qual a duração do sorteio? (s|m|h|d)',
                 'O que vai ser sorteado?']

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

    await ctx.send(
        f"O sorteio será no canal {channel.mention} com duração de {answers[1]} a partir da data dessa mensagen.")

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

    winner = random.choice(users)

    await channel.send(f"Parabéns {winner.mention}! Você ganhou {prize}!")


@client.command(aliases=['Clear', 'clear', 'purge', 'Purge'])
@commands.has_role("Helpers")
async def clear_messages(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Foram apagadas {amount} mensagens.')


client.run(os.environ['token'])
