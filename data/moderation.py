import discord
import asyncio
from discord.ext import commands

class Moderation:
  def __init__(self, bot):
    self.bot = bot
  
  async def on_message(self, message):
    if message.author.bot:
      return
    if "537014667550261318" in(message.server.id):
      if "537921057005371402" in(message.channel.id):
        if message.content.startswith('!invites'):
          return
        else:
          await self.bot.delete_message(message)
          
      if "537921215168512000" in(message.channel.id):
        await self.bot.delete_message(message)
        return
      
      if ('@everyone') in message.content:
        if "538056427374379008" in(role.id for role in message.author.roles):
          return
        
        await self.bot.delete_message(message)
        embed=discord.Embed(title=" ", description=" ", color=0xdb781e)
        embed.set_footer(text='developer: Prisa')
        embed.set_author(name="Warn", icon_url=message.author.avatar_url)
        embed.set_image(url=" ")
        embed.add_field(name="User", value=" {} ".format(message.author.mention), inline=True)
        embed.add_field(name="Reason", value="mention **everyone** \n"
                        "user doesn´t have **<@&538056427374379008> role**", inline=True)
        embed.add_field(name="Info", value="message was deleted", inline=True)
        await self.bot.send_message(discord.Object(id='537919645387194371'), embed=embed)
        
        embed=discord.Embed(title=" ", description=" ", color=0xdb781e)
        embed.set_footer(text='developer: Prisa')
        embed.set_author(name="Warn", icon_url=message.author.avatar_url)
        embed.set_image(url=" ")
        embed.add_field(name="User", value=" {} ".format(message.author.mention), inline=True)
        embed.add_field(name="Reason", value="mention **everyone** \n"
                        "You don´t have **10 invites role**", inline=True)
        embed.add_field(name="**Info**", value="just read <#528148347698020353> ", inline=False)
        await self.bot.send_message(message.author, embed=embed)
        return
      
      if ('@here') in message.content:
        if "538056427374379008" in(role.id for role in message.author.roles):
          return
        
        await self.bot.delete_message(message)
        embed=discord.Embed(title=" ", description=" ", color=0xdb781e)
        embed.set_footer(text='developer: Prisa')
        embed.set_author(name="Warn", icon_url=message.author.avatar_url)
        embed.set_image(url=" ")
        embed.add_field(name="User", value=" {} ".format(message.author.mention), inline=True)
        embed.add_field(name="Reason", value="mention **here** \n"
                        "user doesn´t have **<@&538056427374379008> role**", inline=True)
        embed.add_field(name="Info", value="message was deleted", inline=True)
        await self.bot.send_message(discord.Object(id='537919645387194371'), embed=embed)
        
        embed=discord.Embed(title=" ", description=" ", color=0xdb781e)
        embed.set_footer(text='developer: Prisa')
        embed.set_author(name="Warn", icon_url=message.author.avatar_url)
        embed.set_image(url=" ")
        embed.add_field(name="User", value=" {} ".format(message.author.mention), inline=True)
        embed.add_field(name="Reason", value="mention **here** \n"
                        "You don´t have **10 invites role**", inline=True)
        embed.add_field(name="**Info**", value="just read <#528148347698020353> ", inline=False)
        await self.bot.send_message(message.author, embed=embed)
        return
      
      if ('discord.gg') in message.content:
        if "537914257639997441" in(role.id for role in message.author.roles):
          if "537924101227020288" in(message.channel.id):
            return
          if "538057195871535135" in(message.channel.id):
            return
          
          await self.bot.delete_message(message)
          embed=discord.Embed(title=" ", description=" ", color=0xdb781e)
          embed.set_footer(text='developer: Prisa')
          embed.set_author(name="Warn", icon_url=message.author.avatar_url)
          embed.set_image(url=" ")
          embed.add_field(name="User", value=" {} ".format(message.author.mention), inline=True)
          embed.add_field(name="Reason", value="🔗post invite link \n"
                          "in <#{}> ".format(message.channel.id), inline=True)
          embed.add_field(name="Info", value="message was deleted", inline=True)
          await self.bot.send_message(discord.Object(id='537919645387194371'), embed=embed)
          
          embed=discord.Embed(title=" ", description=" ", color=0xdb781e)
          embed.set_footer(text='developer: Prisa')
          embed.set_author(name="Warn", icon_url=message.author.avatar_url)
          embed.set_image(url=" ")
          embed.add_field(name="User", value=" {} ".format(message.author.mention), inline=True)
          embed.add_field(name="Reason", value="🔗post invite link \n"
                          "please post your invite links only in <#528156791725490186>", inline=True)
          await self.bot.send_message(message.author, embed=embed)
          return
          
        else:
          await self.bot.delete_message(message)
          embed=discord.Embed(title=" ", description=" ", color=0xdb781e)
          embed.set_footer(text='developer: Prisa')
          embed.set_author(name="Warn", icon_url=message.author.avatar_url)
          embed.set_image(url=" ")
          embed.add_field(name="User", value=" {} ".format(message.author.mention), inline=True)
          embed.add_field(name="Reason", value="🔗post invite link \n"
                          "user doesn´t have **Verified** account", inline=True)
          embed.add_field(name="Info", value="message was deleted", inline=True)
          await self.bot.send_message(discord.Object(id='537919645387194371'), embed=embed)
          
          embed=discord.Embed(title=" ", description=" ", color=0xdb781e)
          embed.set_footer(text='developer: Prisa')
          embed.set_author(name="Warn", icon_url=message.author.avatar_url)
          embed.set_image(url=" ")
          embed.add_field(name="User", value=" {} ".format(message.author.mention), inline=True)
          embed.add_field(name="Reason", value="🔗post invite link \n"
                          "You don´t have **Verified** account ", inline=True)
          embed.add_field(name="**Info**", value="Just **verify your account** in <#528209980734832642> \n"
                          "with **.verify** command", inline=False)
          await self.bot.send_message(message.author, embed=embed)
          return
          
  @commands.command(pass_context=True)
  async def warn(self, ctx, user: discord.User, *, reason=""):
    if "537913297052106762" in(role.id for role in ctx.message.author.roles):
      mod = "537913297052106762"
    if "537913808975429642" in(role.id for role in ctx.message.author.roles):
      mod = "537913808975429642"
    if mod in(role.id for role in ctx.message.author.roles):
      await self.bot.delete_message(ctx.message)
      embed=discord.Embed(title=" ", description=" ", color=0xdb781e)
      embed.set_footer(text='developer: Prisa')
      embed.set_author(name="Warn", icon_url=user.avatar_url)
      embed.set_image(url=" ")
      embed.add_field(name="User", value=" {} ".format(user.mention), inline=True)
      embed.add_field(name="Reason", value="{}".format(reason), inline=True)
      embed.add_field(name="Moderator", value=" {} ".format(ctx.message.author.mention), inline=True)
      await self.bot.send_message(discord.Object(id='537919645387194371'), embed=embed)
      
      embed=discord.Embed(title=" ", description=" ", color=0xdb781e)
      embed.set_footer(text='developer: Prisa')
      embed.set_author(name="Warn", icon_url=user.avatar_url)
      embed.set_image(url=" ")
      embed.add_field(name="User", value=" {} ".format(user.mention), inline=True)
      embed.add_field(name="Warned for", value="{}".format(reason), inline=False)
      await self.bot.send_message(user, embed=embed)
      return
    else:
      return
    
  @commands.command(pass_context=True)
  async def report(self, ctx, user: discord.User, *, reason=""):
    if "537913978479837194" in(role.id for role in ctx.message.author.roles):
      mod = "537913978479837194"
    if "537914257639997441" in(role.id for role in ctx.message.author.roles):
      mod = "537914257639997441"
    if mod in(role.id for role in ctx.message.author.roles):
      await self.bot.delete_message(ctx.message)
      embed=discord.Embed(title=" ", description=" ", color=0xdb781e)
      embed.set_footer(text='developer: Prisa')
      embed.set_author(name="Report", icon_url=user.avatar_url)
      embed.set_image(url=" ")
      embed.add_field(name="User", value=" {} ".format(user.mention), inline=True)
      embed.add_field(name="Reason", value="{}".format(reason), inline=True)
      embed.add_field(name="Reported by", value=" {} \n"
                      "Role : <@&{}> ".format(ctx.message.author.mention, mod), inline=True)
      await self.bot.send_message(discord.Object(id='537919710713610250'), embed=embed)
    
def setup(bot):
  bot.add_cog(Moderation(bot))

