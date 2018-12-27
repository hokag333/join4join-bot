import discord
from discord.ext import commands

class Level:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(pass_context=True)
  async def pf(self, ctx, user: discord.User=None):
    
def setup(bot):
  bot.add_cog(Level(bot))
