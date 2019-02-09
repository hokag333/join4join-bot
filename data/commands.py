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
    if "537913297052106762" in(role.id for role in ctx.message.author.roles):
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
    if "537913297052106762" in(role.id for role in ctx.message.author.roles):
      mod = "537913297052106762"
      
    if "537913808975429642" in(role.id for role in ctx.message.author.roles):
      mod = "537913808975429642"
    
    if mod in(role.id for role in ctx.message.author.roles):
      if "537923962659667969" in(ctx.message.channel.id):
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.channel, "**__Help__** \n"
                                    "**            **If you need help with something write **.help** and <@538781726319837184> bot will help you \n"
                                    "**            **or contact <@&537913808975429642> or <@&537915611205074947> \n"
                                    "**            **all messages in this channel will be cleaned every week")
        return
      
  @commands.command(pass_context=True)
  async def partnership(self, ctx, reason=None):
    if reason == "join":
      await self.bot.send_message(ctx.message.channel, "partnership program is in setting")
      return
    if not reason:
      embed = discord.Embed(title = '**__Partnership program__**', description = ' ', colour = discord.Colour.purple())
      embed.set_footer(text='developer: Prisa#4835')
      embed.set_thumbnail(url='')
      embed.set_image(url='')
      embed.set_author(name='', icon_url='')
      embed.add_field(name='**How does it work**', value= "If you invite **Join4Join** bot to your server \n"
                      "your server will be automatically connected to **Partnership program** \n"
                      "after this, bot will automatically inviting members to your server \n"
                      "**  ____  **", inline=True)
      embed.add_field(name="function", value= "if **member join** your server, \n"
                      "bot will invite him to **join4join** server \n"
                      "and invite one random member of **Join4Join** server to your server \n"
                      "(if member is already on **Join4Join** server, function will be skipped)"
                      "**     **", inline=False)
      embed.add_field(name='**fake invites**', value= "if you will making fake invites \n"
                      "**Partnership** program will be disabled on your server \n"
                      "**  ____   **", inline=True)
      embed.add_field(name='**.partnership join**', value= 'invite **join4join** bot to your server', inline=False)
      await self.bot.send_message(ctx.message.channel, embed=embed)
      return
    
def setup(bot):
  bot.add_cog(Commands(bot))
