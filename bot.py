import Chat
import youtube_dl
import Music

from discord.ext import commands

import bot_token

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='nithin\'s personal music/fun bot')




bot.add_cog(Music.Music(bot))
bot.add_cog(Chat.Chat(bot))
bot.run(bot_token.get_token())