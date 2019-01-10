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
    members = ["text", "hi", "lol"]
    server = ctx.message.server
    await self.bot.send_message(ctx.message.channel, "test {}".format(random.choice(members)))
    await self.bot.send_message(ctx.message.channel, "test {}".format(random.choice(server.members).mention))
    return
  
  @commands.command(pass_context=True)
  async def mytestcmd(self, ctx):
    await self.bot.send_message(ctx.message.channel, "reward roles \n"
                               "10 invites = mention everyone \n"
                               "20 invites = dm random members to join4join \n"
                               "**this is test** ")
    return
    
  @commands.command(pass_context=True)
  async def clear(self, ctx, amount=10):
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
