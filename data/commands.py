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
  async def dm(self, ctx):
    user = random.choice(ctx.message.server.members)
    await self.bot.send_message(ctx.message.channel, " {} ".format(user.mention))
   
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
      
        
    
def setup(bot):
  bot.add_cog(Commands(bot))
