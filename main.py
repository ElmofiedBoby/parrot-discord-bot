import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
import requests
import os
import music

client = discord.Client()
bot = commands.Bot(command_prefix="!")

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
    
    if message.content.startswith('!download'):
        os.system('rm song.*')
        music.play(message.content[6:])

    #if message.content.startswith('!play'):



@client.event
async def on_reaction_add(reaction, user):
    quotes = client.get_channel(888832318511386644)
    if user.bot:
        return
    if reaction.emoji == '\U0001F4F8':
        await quotes.send("\"{0}\" -{1}".format(reaction.message.content, reaction.message.author))

client.run(os.getenv('TOKEN'))