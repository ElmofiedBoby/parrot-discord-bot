import discord
from discord.ext.commands import bot
from discord.ext import commands

class Chat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:
            return

        if "cringe" in message.content:
            emoji_disgust = '\U0001F922'
            await message.add_reaction(emoji_disgust) # 🤢

        if message.content.startswith('b') or message.content.startswith('B'):
            emoji_b = '\U0001F171' # 🅱
            await message.add_reaction(emoji_b)