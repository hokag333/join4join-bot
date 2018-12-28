import discord
from discord.ext import commands

class Commands:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(pass_context=True)
  async def dm(self):
    await self.bot.say("test")
    
def setup(bot):
  bot.add_cog(Commands(bot))
