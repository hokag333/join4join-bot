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
  async def tre(self, ctx):
    await self.bot.send_message(ctx.message.channel, "not set")
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
    
  @commands.command(pass_context=True)
  async def definition(self, ctx):
    if "528145435022327810" in(role.id for role in ctx.message.author.roles):
      mod = "528145435022327810"
      
    if "528200802863677450" in(role.id for role in ctx.message.author.roles):
      mod = "528200802863677450"
    
    if mod in(role.id for role in ctx.message.author.roles):
      if "529265526002941953" in(ctx.message.channel.id):
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, "**__Help__** \n"
                                    "**            **If you need help with something write **.help** and <@522411754731339786> bot will help you \n"
                                    "**            **or contact <@&528200802863677450> or <@&529619823404253184> \n"
                                    "**            **messages in this channel will be every week cleaned")
        return
    
def setup(bot):
  bot.add_cog(Commands(bot))
