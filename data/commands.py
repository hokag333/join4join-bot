import discord
from discord.ext import commands

class Commands:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(pass_context=True)
  async def dm(self, ctx):
    await self.bot.send_message(ctx.message.channel, "test message, message by {}".format(ctx.message.author.mention))
    
  @commands.command(pass_context=True)
  async def verify(self, ctx):
    await self.bot.delete_message(ctx.message)
    await self.bot.send_message(ctx.message.channel, " {} waiting for verification".format(ctx.message.author.mention)
    
def setup(bot):
  bot.add_cog(Commands(bot))
