import discord
import asyncio
import random
import itertools, datetime
from async_timeout import timeout
from discord.ext import commands

class Commands:
  def __init__(self, bot):
    self.bot = bot
    
  async def on_command_error(self, error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
      message = content="You have %.5s s cooldown on this command" % error.retry_after
      await self.bot.send_message(ctx.message.channel, message)
      raise error
      
  @commands.command(pass_context=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def dm(self, ctx, *, reason=""):
    if "528160233273425923" in(role.id for role in ctx.message.author.roles):
      await self.bot.delete_message(ctx.message)
      await self.bot.send_message(ctx.message.channel, "{}\n"
                                  " \n"
                                  "**Join 4 Join dm** by {} \n"
                                  "don´t forget to contact him to make join 4 join".format(reason, ctx.message.author.mention))
      return
    if "528500676372856834" in(role.id for role in ctx.message.author.roles):
      await self.bot.delete_message(ctx.message)
      await self.bot.send_message(ctx.message.channel, "{}\n"
                                  " \n"
                                  "**Join 4 Join dm** by {} \n"
                                  "don´t forget to contact him to make join 4 join".format(reason, ctx.message.author.mention))
      return
    else:
      await self.bot.send_message(ctx.message.channel, "{} you don´t have permissions to dm command".format(ctx.message.author.mention))
   
  @commands.command(pass_context=True)
  async def clear(self, ctx, amount=51):
    if "528145435022327810" in(role.id for role in ctx.message.author.roles):
      channel = ctx.message.channel
      messages = []
      async for message in self.bot.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
        await self.bot.delete_messages(messages)
        msg = "**{}** messages was deleted".format(amount)
        await self.bot.send_message(ctx.message.channel, msg)
        return
      
  @commands.command(pass_context=True)
  async def infodm(self, ctx, *, reason=""):
    if "458341993328803850" in(role.id for role in ctx.message.author.roles):
      user = ["381887710308335618", "522818952464695316"]
      member = random.choice(user)
      await self.bot.send_message(discord.Object(id='529944759364747264'), ".test <@{}>".format(member))
      return
  
  @commands.command(pass_context=True)
  async def test(self, ctx, user: discord.User, *, reason=""):
    if ctx.message.author.bot:
      await self.bot.send_message(user, "test")
      
        
    
def setup(bot):
  bot.add_cog(Commands(bot))
