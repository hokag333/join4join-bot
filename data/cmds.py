import discord
from discord.ext import commands

class Cmds:
  def __init__(self, bot):
    self.bot = bot
    
    
  @commands.command(pass_context=True)
  async def dm(self, ctx):
    await self.bot.send_message(ctx.message.channel," test dm \n"
                                "by user {} ".format(ctx.message.author.mention)

    
    
def setup(bot):
  bot.add_cog(Cmds(bot))
