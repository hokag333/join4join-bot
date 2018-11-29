import discord
from discord.ext import commands

class Pic:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.content.startswith('embed'):
      await self.bot.send_message(message.channel, 'it is not set')
      
  @commands.command()
  async def testall(self):
    await self.bot.say('lol')
    
def setup(bot):
  bot.add_cog(Pic(bot))
