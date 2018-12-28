import discord
from discord.ext import commands

class Commands:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(pass_context=True)
  async def dm(self, ctx):
    await self.bot.say(" {}".format(ctx.message.author.mention)
    
def setup(bot):
  bot.add_cog(Commands(bot))
