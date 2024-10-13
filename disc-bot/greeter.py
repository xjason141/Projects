import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHL_ID = os.getenv('CHANNEL_TOKEN')

# set prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.command()
async def fl(ctx):
    channel = bot.get_channel(CHL_ID)
    await channel.send('Hello Lexdomo.')

@bot.command()
async def fn(ctx):
    channel = bot.get_channel(CHL_ID)
    await channel.send('Hello Lala.')

@bot.command()
async def fd(ctx):
    channel = bot.get_channel(CHL_ID)
    await channel.send('Hello Didi.')

# fetch images
@bot.command()
async def sad(ctx):
    url_list = ['https://tenor.com/view/sad-pout-pout-anime-pouting-my-dress-up-darling-gif-7117836254488094139',
                'https://media.tenor.com/Iy7uWP17ZvQAAAAM/anime-sad.gif',
                'https://tenor.com/view/pokemon-pikachu-upset-sad-anime-gif-22961752',
                'https://tenor.com/view/anime-gif-10271429305488134245',
                'https://tenor.com/view/aya-asagiri-asagiri-sad-anime-girl-sad-sad-anime-gif-15837535968675553521',
                'https://tenor.com/view/terrified-panic-anime-girl-chibi-gif-1493101046335227175',
                'https://tenor.com/view/sad-anime-boy-gif-23701094',
                'https://tenor.com/view/anime-cry-missing-want-hug-sad-cry-gif-16168198606411323098',
                'https://tenor.com/view/anime-my-star-depressed-rain-raining-gif-7225202150109634836',
                'https://tenor.com/view/juvia-juvia-lockser-fairy-tail-anime-tears-crying-eyes-gif-8899647780846351004',
                'https://tenor.com/view/pink-hair-anime-girl-anya-anya-forger-anya-spy-x-family-anime-anya-spy-x-family-gif-25670093',
                'https://tenor.com/view/girl-sad-fake-smile-fake-anime-gif-12232121499355742379',
                'https://tenor.com/view/frieren-%E8%91%AC%E9%80%81%E3%81%AE%E3%83%95%E3%83%AA%E3%83%BC%E3%83%AC%E3%83%B3-sousou-no-frieren-sousou-beyond-journey\'s-end-gif-13214487266596803271'
                ]
    # channel = bot.get_channel(CHL_ID)
    # async with aiohttp.ClientSession() as session:
    #     async with session.get(url_list[0]) as resp:
    #         img = await resp.read()
    #         with io.BytesIO(img) as file:
    #             await ctx.send(file=discord.File(file, 'anime.png'))
    await ctx.send(url_list[random.randint(0, len(url_list)-1)])


bot.run(BOT_TOKEN)