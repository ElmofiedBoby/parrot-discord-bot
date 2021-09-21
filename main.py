import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if "cringe" in message.content:
        emoji_disgust = '\U0001F922'
        await message.add_reaction(emoji_disgust) # 🤢

    if message.content.startswith('b') or message.content.startswith('B'):
        emoji_b = '\U0001F171' # 🅱
        await message.add_reaction(emoji_b)

@client.event
async def on_reaction_add(reaction, user):
    quotes = client.get_channel(888832318511386644)
    if user.bot:
        return
    # I do not actually recommend doing this.
    if reaction.emoji == '\U0001F4F8':
        await quotes.send("\"{0}\" -{1}".format(reaction.message.content, reaction.message.author))



client.run(os.getenv('TOKEN'))