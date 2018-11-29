import discord
from discord.ext import commands

class Reply:
  def __init__(self, bot):
    self.bot = bot
    
  
  async def on_message(self, message):
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
      
    if message.content.startswith('duck'):
      await bot.send_message(message.channel, 'quack')
      
    if message.content.startswith('knock knock'):
      await bot.send_message(message.channel, 'who is there?!')
      
    if message.content.startswith('Hey!'):
      await bot.send_message(message.channel, 'Yeah boy')
      
    if message.content.startswith('train'):
      await bot.send_message(message.channel, ':bullettrain_front:')
      
    if message.content.startswith('good night'):
      await bot.send_message(message.channel, '<:sleepingegg:508556018779947030>')
      
    if message.content.startswith('ho is playing in the beginning'):
      await bot.send_message(message.channel, 'EMINƎM')
      
  @commands.command()
  async def ping(self):
    await self.bot.say('bang')
    
def setup(bot):
  bot.add_cog(Reply(bot))
