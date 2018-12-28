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
    await self.bot.send_message(ctx.message.channel, " {} waiting for verification".format(ctx.message.author.mention))
    
  @commands.command(pass_context=True)
  async def verified(self, ctx, user: discord.User):
    if "528145435022327810" in(role.id for role in ctx.message.author.roles):
      await self.bot.send_message(user, "{} verification complete \n"
                                  "You can now post invite links in **Join 4 Join** server \n"
                                  "You was verificate by {}".format(user.mention, ctx.message.author.mention))
    
def setup(bot):
  bot.add_cog(Commands(bot))
