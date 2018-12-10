import discord
import asyncio
import youtube_dl
import os
from discord.ext import commands
from discord.ext.commands import Bot


bot=commands.Bot(command_prefix='!')
bot.remove_command('help')

extensions = ['reply', 'pic', 'data.tier', 'help', 'data.points']

@bot.event
async def on_ready():
  await bot.change_presence(game=discord.Game(name='Chicken Server'))
  print('Bot is ready.')
  
if __name__ == '__main__':
  for extension in extensions:
    try:
      bot.load_extension(extension)
    except Exception as error:
      print('{} cannot be loaded. [{}]'.format(extension, error))

bot.run(os.environ['BOT_TOKEN'])
