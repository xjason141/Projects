import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv


# set bot token and channel ID
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHL_ID = os.getenv('MAIN_CHL')

# set prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# says hi when bot goes online
@bot.event
async def on_ready():
    chl = bot.get_channel(int(CHL_ID))
    await chl.send('Hey there. I\'m ready to go.')


# greets the users
@bot.command()
async def fl(ctx):
    channel = bot.get_channel(int(CHL_ID))
    await channel.send('Hello Lexdomo.')

@bot.command()
async def fn(ctx):
    channel = bot.get_channel(int(CHL_ID))
    await channel.send('Hello Lala.')

@bot.command()
async def fd(ctx):
    channel = bot.get_channel(int(CHL_ID))
    await channel.send('Hello Didi.')


# below are commands to show gifs based on emotions
# emotion: sad
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
    await ctx.send(url_list[random.randint(0, len(url_list)-1)])

# emotion: happy
@bot.command()
async def happy(ctx):
    url_list =['https://tenor.com/view/gojo-satoru-gojo-satoru-jjk-jujutsu-kaisen-gif-7280593681001594903',
               'https://tenor.com/view/chika-yeah-happy-spinning-cgeerful-gif-17862523',
               'https://tenor.com/view/excited-anime-cute-spy-x-family-gif-26845849',
               'https://tenor.com/view/anime-kubo-san-happy-gif-27394281',
               'https://tenor.com/view/anime-frieren-hehe-he-he-he-gif-8238190512466196205',
               'https://tenor.com/view/yaay-anime-girl-happy-anime-girl-yay-yay-anime-yay-gif-25826464',
               'https://tenor.com/view/anime-gif-25501630',
               'https://tenor.com/view/shake-kaninayuta-nayutakani-nayuta-kani-gif-15120516202578591549',
               'https://tenor.com/view/dance-happy-cute-menhera-chan-gif-19487018',
               'https://tenor.com/view/mysticlight-fox-vtuber-fox-girl-envtuber-mysticlight-bounce-gif-5498176757132986538'
               ]
    await ctx.send(url_list[random.randint(0, len(url_list)-1)])

# emotion: surprised
@bot.command()
async def shock(ctx):
    url_list =['https://tenor.com/view/sousou-no-frieren-frieren-beyond-journey-frieren-anime-frieren-book-drop-book-dropping-gif-5586080115796339217',
               'https://tenor.com/view/bocchi-the-rock-bocchi-shocked-bocchi-shock-face-anime-shocked-face-bocch-the-rock-shocked-gif-27050901',
               'https://tenor.com/view/mahjong-hyakuman-great-teacher-onizuka-shocked-anime-surprised-gif-25458883',
               'https://tenor.com/view/spy-x-family-anime-anya-forger-shock-what-gif-25492650',
               'https://tenor.com/view/anime-gon-what-shocked-surprised-gif-16031757',
               'https://tenor.com/view/azumanga-daioh-chiyo-chan-anime-reaction-surprised-gif-15240705844533310378',
               'https://tenor.com/view/watayuri-watashi-no-yuri-wa-oshigoto-desu-yuri-is-my-job-anime-yuri-gif-11755048074768834244',
               'https://tenor.com/view/maomao-anime-jinshi-shocked-maomao-shocked-gif-17933671686991107481',
               'https://tenor.com/view/sung-jin-woo-solo-leveling-afraid-anime-fantasy-gif-5162571057710275723',
               'https://tenor.com/view/mahito-jjk-jjk-s2-mahito-mahito-scared-anime-scared-gif-6256141653869631072'
               ]
    await ctx.send(url_list[random.randint(0, len(url_list)-1)])

# emotion: disappointed
@bot.command()
async def bruh(ctx):
    url_list =['https://tenor.com/view/anime-fern-anger-angry-annoyed-gif-5137243747516951410',
               'https://tenor.com/view/yuki-kaguya-shinomiya-gif-24132804',
               'https://tenor.com/view/my-honest-reaction-my-honest-reaction-one-piece-luffy-gif-25285852',
               'https://tenor.com/view/disappointed-not-surprised-death-note-l-lawliet-anime-gif-17134977',
               'https://tenor.com/view/bocchi-bocchi-the-rock-nijika-anime-anime-girl-gif-3727459729326210548',
               'https://tenor.com/view/disappointed-disgusting-hyolan-wolf-dog-gif-27271273',
               'https://tenor.com/view/bocchi-bocchi-the-rock-nijika-angry-scary-stare-gif-15418130218235280496',
               'https://tenor.com/view/anime-tempura-fail-disappointed-gif-23617983',
               'https://tenor.com/view/what-disappointed-anime-angry-gif-17844136',
               'https://tenor.com/view/anime-yui-hirasawa-disappointment-gif-15673751'
               ]
    await ctx.send(url_list[random.randint(0, len(url_list)-1)])

# emotion: angry
@bot.command()
async def angry(ctx):
    url_list =['https://tenor.com/view/anime-aaaa-yelling-scream-mad-gif-2566373336159153327',
               'https://tenor.com/view/mad-anime-anime-girl-mad-black-mad-black-anime-gif-9801680199954311748',
               'https://tenor.com/view/angry-gif-6367919497800974711',
               'https://tenor.com/view/yor-yor-anime-angry-yor-angry-anime-anime-angry-gif-12180248608896266854',
               'https://tenor.com/view/huh-angry-anime-gif-16249071634720471704',
               'https://tenor.com/view/anime-evil-sight-anger-angry-gif-4896687546701460935',
               'https://tenor.com/view/insane-mad-angry-triggered-hyolan-gif-27271284',
               'https://tenor.com/view/angry-mad-trigger-anime-gif-18499756',
               'https://tenor.com/view/angry-gif-5267681033793712859',
               'https://tenor.com/view/emojify-gif-21039591'
               ]
    await ctx.send(url_list[random.randint(0, len(url_list)-1)])



# explaination on available commands
@bot.command()
async def cmds(ctx):
    await ctx.send('''
        1. !fl = returns 'Hello Lexdomo.'
        \n2. !fn = returns 'Hello Lala.'
        \n3. !fd = returns 'Hello Didi.'
        \n4. !happy = returns a random happy anime gif 
        \n5. !sad = returns a random sad anime gif 
        \n6. !shock = returns a random shock anime gif 
        \n7. !bruh = returns a random disappoint anime gif
        ''')

run = bot.run(BOT_TOKEN)

if __name__ == '__main__':
    run