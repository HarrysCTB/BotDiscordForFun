import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import random
import asyncio


class ClassRass:
    def __init__(self, c_mention):
        self.mention = c_mention
        self.addcheck = False
        self.channelid = ""

# <---------------------- Variable ---------------------->

client = commands.Bot(command_prefix='/', intents=discord.Intents.all())
cmd = {}
listUser = []
test = ClassRass(listUser)


# <---------------------- Option ---------------------->


@client.event
async def on_ready():
    print("Success: Bot is connected to Discord")


# <---------------------- Commande textuelle ---------------------->


@client.command()
async def update(ctx):
    await ctx.send(f"Bonjour {ctx.message.author.mention}, voici la mise à jour **1.0** :robot: !\n"
                   f"\n"
                   f"`• Ajout de la fonction « /rassemblement », Capacité future de créer des groupes, de sauvegarder la création de groupes et de gérer les erreurs.\n"
                   f"• Ajout de la fonction « /rassemblement », Capacité future de créer des groupes, de sauvegarder la création de groupes et de gérer les erreurs.\n"
                   f"• Ajout de la fonction « /rassemblement », Capacité future de créer des groupes, de sauvegarder la création de groupes et de gérer les erreurs.\n"
                   f"• Ajout de la fonction « /rassemblement », Capacité future de créer des groupes, de sauvegarder la création de groupes et de gérer les erreurs.`")


@client.command()
async def infocmd(ctx):
    await ctx.send(f"Bonjour {ctx.message.author.mention}, voici la liste des commandes que tu peux effectuer :mechanical_arm: !\n"
                   f"\n"
                   f"• `/insulte` : Permets d'insulter la grand-mère à un utilisateur, l'usage se fait par `/insulte <mention de l'utilisateur>` :face_with_symbols_over_mouth:\n"
                   f"• `/infocmd` : Tu viens de l'utiliser quand même... :turkey: \n"
                   f"• `/jugement` : Permets de lancer un jugement d'un utilisateur afin de l'exclure temporairement, `/jugement <mention de l'utilisateur` puis voter pour la sentence :scales:\n"
                   f"• `/` : SOON :construction:\n"
                   f"• `/update` : Permets de voir les avancées de mes fonctionnalités :robot:\n"
                   f"• `/addrassemblement` : Permets de rajouter un utilisateur au `/rassemblement`, l'usage se fait par`/addrassemblement <mention de l'utilisateur>`.\n"
                   f"• `/rassemblement` :  Permets de lancer un « Aux armes :white_circle: :blue_circle: » afin de regrouper ses amis dans un canal vocal, `/rassemblement`")

# <---------------------- Insulte ---------------------->


@client.command()
async def insulte(ctx, question):
    if question[1] == '@':
        with open('listOfInsult') as f:
            lines = f.read().splitlines()
        await ctx.send(random.choice(lines) + f" {question}", tts=True)
    else:
        await ctx.send("oui oui et @Tarzan aussi ?", tts=True)

# <---------------------- Rassemblement ---------------------->

@client.command()
async def addrassemblement(ctx, Member: discord.Member):
    test.mention.append(Member)
    test.addcheck = True


@client.command()
async def rassemblement(ctx):
    if ctx.message.author.voice and test.addcheck is False:
        await ctx.send("erreur rassemblement")
    else:
        if ctx.message.author.voice:
            channel = client.get_channel(ctx.message.author.voice.channel.id)
            link = await channel.create_invite(max_age=3600, max_uses=1, unique=True)
            for elem in test.mention:
                await elem.send(link)
        else:
            await ctx.send("nul")

# <---------------------- Jugement ---------------------->


@client.command()
async def jugement(ctx, Member: discord.Member):
    message = await ctx.send(f"{Member.mention} mérite-t-il d'aller voir ailleurs ?")
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    timer_duration_seconds = 10
    await ctx.send(f'Minuteur démarré pour X minutes.')
    await asyncio.sleep(timer_duration_seconds)
    message2 = await ctx.channel.fetch_message(message.id)
    reactions = message2.reactions
    reaction_list = [f'{reaction.emoji}: {reaction.count}' for reaction in reactions]
    await ctx.send('\n'.join(reaction_list))
    await ctx.send('Le temps est écoulé !')


# <---------------------- Private cmd ---------------------->

@client.command()
async def private(ctx):
    await ctx.send("disponiblie prochainement :construction: !")


# <---------------------- Run ---------------------->

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client.run(token)
