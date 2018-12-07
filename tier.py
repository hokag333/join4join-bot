import discord
from discord.ext import commands

class Tier:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.author.bot: return
      
    if message.content.startswith('astabagar'):
      await self.bot.send_message(message.channel, 'new Class tested')
      
      
  @commands.command()
  async def trtierewsi(self):
    await self.bot.say('bang')
        
        
def setup(bot):
  bot.add_cog(Tier(bot))
