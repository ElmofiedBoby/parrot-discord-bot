import asyncio
import discord
import YTDLSource
import queue_tracker as q
from discord.ext import commands


class Music(commands.Cog):

    client = discord.Client()

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def join(self, ctx):

        if not ctx.message.author.voice:
            await ctx.send("You are not connected to a voice channel!")
            return
        else:
            channel = ctx.message.author.voice.channel
            self.queue = {}
            await ctx.send(f'Connected to ``{channel}``')

        await channel.connect()

    @commands.command()
    async def play(self, ctx, *, url):

        try:

            async with ctx.typing():
                player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)

                if len(self.queue) == 0:

                    self.start_playing(ctx.voice_client, player)
                    await ctx.send(f':mag_right: **Searching for** ``' + url + '``\n<:youtube:763374159567781890> **Now Playing:** ``{}'.format(player.title) + "``")

                else:
                    
                    self.queue[len(self.queue)] = player
                    await ctx.send(f':mag_right: **Searching for** ``' + url + '``\n<:youtube:763374159567781890> **Added to queue:** ``{}'.format(player.title) + "``")

        except:

            await ctx.send("Somenthing went wrong - please try again later!")

    def start_playing(self, voice_client, player):

        self.queue[0] = player

        i = 0
        while i <  len(self.queue):
            try:
                voice_client.play(self.queue[i], after=lambda e: print('Player error: %s' % e) if e else None)

            except:
                pass
            i += 1