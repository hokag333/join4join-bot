import discord
import asyncio
import itertools, datetime
from async_timeout import timeout
from discord.ext import commands

class Commands:
  def __init__(self, bot):
    self.bot = bot
    
  async def on_message(self, message):
    if ('discord.gg') in message.content:
      if "528142547894272010" in (ctx.message.server.id):
        if message.author.bot:
          return
        
        if "528162784022626314" in(role.id for role in message.author.roles):
          return
        else:
          await self.bot.delete_message(message)
          await self.bot.send_message(message.channel, " {} you need have verify your account, \n"
                                      "write **.verify** to make verification".format(message.author.mention))
          embed = discord.Embed(title = 'Warn', description = '', colour = discord.Colour.blue())
          embed.set_footer(text='developer: Prisa#4835')
          embed.set_thumbnail(url='')
          embed.set_image(url='')
          embed.set_author(name='', icon_url=ctx.message.author.avatar_url)
          embed.add_field(name='**User**', value= '{}'.format(ctx.message.author.mention), inline=True)
          embed.add_field(name='**reason**', value= 'post invite link', inline=True)
          embed.add_field(name='**Role**', value= '<@&528162784022626314>', inline=False)
          embed.add_field(name='**Not in user roles**', value= '', inline=False)
          await self.bot.send_message(self.bot.get_channel('528915422871945228'), embed=embed)
    
  async def on_command_error(self, error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
      message = content="You have %.5s s cooldown on this command" % error.retry_after
      await self.bot.send_message(ctx.message.channel, message)
      raise error
      
  @commands.command(pass_context=True)
  @commands.cooldown(1, 60*60*24, commands.BucketType.user)
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
  @commands.cooldown(1, 60, commands.BucketType.user)
  async def clear(self, ctx, amount=51):
    channel = ctx.message.channel
    messages = []
    async for message in self.bot.logs_from(channel, limit=int(amount) + 1):
      messages.append(message)
    await self.bot.delete_messages(messages)
    msg = "**{}** messages was deleted".format(amount)
    await self.bot.send_message(channel, msg)
    
    
def setup(bot):
  bot.add_cog(Commands(bot))
