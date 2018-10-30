import discord
import asyncio
import youtube_dl
import os
from discord.ext import commands
from discord.ext.commands import Bot


bot=commands.Bot(command_prefix='!')

from discord import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll',
             'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass

    raise RuntimeError('Could not load an opus lib. Tried %s' %
                       (', '.join(opus_libs)))
load_opus_lib()



@bot.event
async def on_ready():
    print("hi")
opts = {
            'default_search': 'auto',
            'quiet': True,
        }    
    
@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)



players={}
@bot.command(pass_context=True)
async def play(ctx, *,url):
    global play_server
    play_server = ctx.message.server
    voice = bot.voice_client_in(play_server)
    global player
    player = await voice.create_ytdl_player(url,ytdl_options=opts)
    players[play_server.id] = player
    await bot.say ("Music is playing")
    await bot.say ("**__Warning:__** to play next song wait when song end")
    if player.is_live == True:
        await bot.say("Can not play live audio yet.")
    elif player.is_live == False:
        player.start()

@bot.command(pass_context=True)
async def pause(ctx):
    player.pause()
    await bot.say("Music paused")

@bot.command(pass_context=True)
async def resume(ctx):
    player.resume()
    await bot.say("Music resumed")
          
@bot.command(pass_context=True)
async def volume(ctx, vol):
    vol = float(vol)
    vol = player.volume = vol

@bot.command(pass_context=True)
async def helping(ctx):
    await bot.say("Hi, I am official helper of **Chicken server**.")
    await bot.say("What you need help with?")
    await bot.say("Write **!helper** and I will help you")
    
@bot.command(pass_context=True)
async def helper(ctx):
  await bot.say("**Commands:**")
  await bot.say("**         !server-info** = info about Chicken server")
  await bot.say("**         !user-info** = info about user")
  await bot.say("**         !games** = list of all games that can be added to game updates ")
  await bot.say("If you need help with something else, write **!call** to call moderators or helpers")

@bot.command(pass_context=True)
async def games(ctx):
  await bot.say("**__List of supported games:__**                                      **__List of games which can be add:__**                                                                                                                                                                                                                          Counter-Strike: Global Offensive :white_check_mark:                                                       Ark                                                                                                                Fortnite :white_check_mark:                                                                                 Black Desert Online")
  
@bot.command(pass_context=True)
async def etcgames(ctx):
  await bot.say("**__List of games which can be add:__**")
  await bot.say("I am creating a list, just wait!!!")
  await bot.say("Ark")
  await bot.say("Black Desert Online")
  await bot.say("Destiny 2")
  await bot.say("Diablo 3")
  await bot.say("Dota 2")
  await bot.say("Factorio")
  await bot.say("Garry´s Mod")
  await bot.say("Grand Theft Auto 5")
  
@bot.command(pass_context=True)
async def test58(ctx):
  await bot.say("test                                                                                                                                                                                                                          test2")

@bot.command(pass_context=True)
async def call(ctx):
  await bot.say("**Moderators** and **Helpers** was called")
  


bot.run(os.environ['BOT_TOKEN'])
