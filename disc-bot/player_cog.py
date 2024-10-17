import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

class Main(commands.cog):
    def __init__(self, bot):
        self.bot = bot
        self.playing = False
        self.pause = False
        self.queue = []

        self.YDL_SETTINGS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFMPEHG_OPTIONS = {'options': '-vn'}

        self.vc = None
    
    # search the song on youtube and returns the url and song title
    def search_music(self, item):
        with YoutubeDL(self.YDL_SETTINGS) as ydl:
            try:
                info = ydl.extract_info('ytsearch:%s' % item, download=False)['entries'[0]]    
            except Exception:
                return False
        return {'source': info['formats'[0]['url']], 'title': info['title']}
    
    def play_next(self):
        if len(self.queue) > 0:
            self.playing = True
            music_url = self.queue[0][0]['source']
            self.queue.pop(0)
            self.vc.play(discord.FFmpegAudio(music_url, **self.FFMPEHG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.playing = False

    async def play(self, ctx):
        if len(self.queue) > 0:
            self.playing = True
            music_url = self.queue[0][0]['source']

            if self.vc == None or not self.vc.is_connected():
                self.vc = await self.queue[0][1].connect()

                if self.vc == None:
                    await ctx.send('Could not connect to channel.')
            else:
                await self.vc.move_to(self.queue[0][1])
            
            self.queue.pop(0)
            self.vc.play(discord.FFmpegAudio(music_url, **self.FFMPEHG_OPTIONS, after=lambda e: self.play_next()))

        else:
            self.playing = False

    # continue on line below. check play.txt for youtube link guide
    # @commands.command(name='play', aliases=['p', 'playing'], help='Play the selected song from Youtube.')
    
