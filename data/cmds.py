import discord
from discord.ext import commands

class Cmds:
  def __init__(self, bot):
    self.bot = bot
    
    
  @commands.command(pass_context=True)
  async def dm(self, ctx, reason):
    await self.bot.delete_message(ctx.message)
    await self.bot.send_message(ctx.message.channel,"  \n" + reason
                                "by user {} ".format(ctx.message.author.mention)

    
    
def setup(bot):
  bot.add_cog(Cmds(bot))
