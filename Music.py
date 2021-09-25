import asyncio
import discord
import YTDLSource
import queue_tracker as q
from discord.ext import commands

music_queue = []

class Music(commands.Cog):

    client = discord.Client()

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def local(self, ctx, *, query):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format(query))

    @commands.command()
    async def play_download(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""

        async with ctx.typing():
            player = await YTDLSource.YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format(player.title))
    
    @commands.command()
    async def pause(self, ctx):
        """Pauses bot"""
        
        await ctx.voice_client.pause()
    
    @commands.command()
    async def resume(self, ctx):
        """Resumes bot"""

        await ctx.voice_client.resume()

    @commands.command()
    async def queue(self, ctx):
        await ctx.send('Current queue:\n')
        counter = 1
        for player in q.get_list():
            await ctx.send("{0} - {1}".format(counter, player.title))
            counter = counter + 1

    @commands.command()
    async def nowplaying(self, ctx):
        await ctx.send('Now playing: {}'.format(q.get_list()[0].title))

    @commands.command()
    async def skip(self, ctx):
        if(len(q.get_list())==0):
            await ctx.send('Nothing is queued!')
        else:
            for song in q.get_list():
                await ctx.send('Now playing: {}'.format(song.title))
                ctx.voice_client.stop()
                ctx.voice_client.play(song, after=q.remove_queue())        

    @commands.command()
    async def play(self, ctx, *, url):
        player = await YTDLSource.YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
        await ctx.send('Now playing: {}'.format(player.title))
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    @commands.command()
    async def playnext(self, ctx, *, url):
        player = await YTDLSource.YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
        q.add_queue(player)


    @commands.command()
    async def play_queue(self, ctx):

        """Streams from a url (same as yt, but doesn't predownload)"""
        async with ctx.typing():
            #player = await YTDLSource.YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            #await ctx.send('Song queued up : {}'.format(player.title))
            if(len(q.get_list())==0):
                await ctx.send('Nothing is queued!')
            else:
                for song in q.get_list():
                    await ctx.send('Now playing: {}'.format(song.title))
                    ctx.voice_client.play(song, after=q.remove_queue())

        

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send("Changed volume to {}%".format(volume))

    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @playnext.before_invoke
    @play_queue.before_invoke
    @local.before_invoke
    @play.before_invoke
    @play_download.before_invoke
    @volume.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()