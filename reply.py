import discord
from discord.ext import commands

class Reply:
  def __init__(self, bot):
    self.bot = bot
    
  
  async def on_message(self, message):
    if message.content.startswith('test me'):
      await self.bot.send_message(message.channel, 'testing')
      
  @commands.command()
  async def ping(self):
    await self.bot.say('bang')
    
def setup(bot):
  bot.add_cog(Reply(bot))
