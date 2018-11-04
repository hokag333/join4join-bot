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

@bot.event
async def on_message(message):
  channel = message.channel
  if message.content.startswith('test'):
    await bot.send_message(channel, 'I am in testing mode')

@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)



players={}




@bot.command(pass_context=True)
async def testing(ctx):
  await bot.say("testing")
  


bot.run(os.environ['BOT_TOKEN'])
