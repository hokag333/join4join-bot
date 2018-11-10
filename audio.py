import discord
import asyncio
import youtube_dl
import os
from discord.ext import commands
from discord.ext.commands import Bot


bot=commands.Bot(command_prefix='!')
bot.remove_command('help')

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
  if message.content.startswith('egg'):
    await bot.send_message(message.channel, ':egg:')
    
  if message.content.startswith('chicken'):
    await bot.send_message(message.channel, ':hatched_chick:')
    
  if message.content.startswith('shit'):
    await bot.send_message(message.channel, ':poop:')
    
  if message.content.startswith('how are you'):
    await bot.send_message(message.channel, ' ** :hatched_chick: I am fine tnx :hatched_chick: ** ')
    
  if message.content.startswith('How are you'):
    await bot.send_message(message.channel, ' ** :hatched_chick: I am fine tnx :hatched_chick: ** ')
    
  if message.content.startswith('Hi'):
    await bot.send_message(message.channel, ':hatched_chick: **Hello** :hatched_chick: ')
    
  if message.content.startswith('hi'):
    await bot.send_message(message.channel, ':hatched_chick: **Hello** :hatched_chick: ')
    
  if message.content.startswith('whats up'):
    await bot.send_message(message.channel, ' **I am good u** ')
    
  if message.content.startswith('damn'):
    await bot.send_message(message.channel, '**fool**')
    
  if message.content.startswith('owner'):
    await bot.send_message(message.channel, 'The server owner is <@381887710308335618>')
    
  if message.content.startswith('website'):
    await bot.send_message(message.channel, '**server website :** https://chickenserver.wix.com/website')



players={}




@bot.command(pass_context=True)
async def test03(ctx):
  await bot.say("testing")
  
@bot.command(pass_context=True)
async def help(ctx):
  embed = discord.Embed(
    colour = discord.Colour.orange()
  )
  
  embed.set_author(name='Help')
  embed.add_field(name='testing', value='the testing command', inline=False)
  


bot.run(os.environ['BOT_TOKEN'])
