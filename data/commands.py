import discord
from discord.ext import commands

class Commands:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(pass_context=True)
  @commands.cooldown(1, 60, commands.BucketType.user)
  async def dm(self, ctx):
    await self.bot.send_message(ctx.message.channel, "test message, message by {}".format(ctx.message.author.mention))
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send("This command is on cooldown, please retry in {}s.".format(math.ceil(error.retry_after)))
    
  @commands.command(pass_context=True)
  async def verify(self, ctx):
    await self.bot.delete_message(ctx.message)
    await self.bot.send_message(ctx.message.channel, " {} waiting for verification🌀".format(ctx.message.author.mention))
    
  @commands.command(pass_context=True)
  async def verified(self, ctx, user: discord.User):
    if "528145435022327810" in(role.id for role in ctx.message.author.roles):
      await self.bot.send_message(user, "{} verification complete✅ \n"
                                  "You can now post **invite links** in **Join 4 Join** server \n"
                                  " \n"
                                  "You was verificate by {}".format(user.mention, ctx.message.author.mention))
      await self.bot.send_message(ctx.message.channel, "{} was verificate".format(user.mention))
      return
    await self.bot.send_message(ctx.message.channel, "{} you don´t heve permissions to do that".format(ctx.message.author.mention))
    
  @commands.command(pass_context=True)
  async def verifyerror(self, ctx, user: discord.User):
    if "528145435022327810" in(role.id for role in ctx.message.author.roles):
      await self.bot.send_message(user, "❗verification error❗ \n"
                                  "{} you are not **Chicken Server** member \n"
                                  "If you want to get **verification** and enable post **invite links** \n"
                                  " \n"
                                  "Join **Chicken Server** \n"
                                  "https://discord.gg/9hjAVpP".format(user.mention))
      await self.bot.send_message(ctx.message.channel, "{} get verification error message".format(user.mention))
      return
    
def setup(bot):
  bot.add_cog(Commands(bot))
