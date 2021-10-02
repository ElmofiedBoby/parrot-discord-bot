import Chat
import youtube_dl
import Music

from discord.ext import commands

import bot_token

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='nithin\'s personal music/fun bot')

@bot.event
async def on_reaction_add(reaction, user):
    id = 888832318511386644
    quotes = bot.get_channel(888832318511386644)
    if user.bot:
        return
    if reaction.emoji == '\U0001F4F8':
        await quotes.send("\"{0}\" -{1}".format(reaction.message.content, reaction.message.author))

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

bot.add_cog(Music.Music(bot))
bot.add_cog(Chat.Chat(bot))
bot.run(bot_token.get_token())
