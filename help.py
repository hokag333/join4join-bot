import discord
from discord.ext import commands

class Helper:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.author.bot: return
    
    
    if ('!help') in message.content:
      await self.bot.send_message(message.channel, 'helping')
      
      
  @commands.command()
  async def bro(self):
    await self.bot.say('ring')
    
    
def setup(bot):
  bot.add_cog(Helper(bot))
