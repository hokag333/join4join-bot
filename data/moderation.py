import discord
from discord.ext import commands

class Moderation:
  def __init__(self, bot):
    self.bot = bot
  
  async def on_message(self, message):
    if message.author.bot:
      return
    if "528142547894272010" in(message.server.id):
      if "528148608533528596" in(message.channel.id):
        if message.content.startswith('!invites'):
          return
        else:
          await self.bot.delete_message(message)
          
      if "528209980734832642" in(message.channel.id):
        await self.bot.delete_message(message)
        return
        
      if ('discord.gg') in message.content:
        if "528162784022626314" in(role.id for role in message.author.roles):
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
          await self.bot.send_message(discord.Object(id='528915422871945228'), embed=embed)
          await self.bot.send_message(message.channel, " {} you need have **verification account**, \n"
                                      "write **.verify** to make verification".format(message.author.mention))
          
  @commands.command(pass_context=True)
  async def warn(self, ctx, user: discord.User, *, reason=""):
    if "528145435022327810" in(role.id for role in ctx.message.author.roles):
      mod = "528145435022327810"
    if "528200802863677450" in(role.id for role in ctx.message.author.roles):
      mod = "528200802863677450"
    if mod in(role.id for role in ctx.message.author.roles):
      await self.bot.delete_message(ctx.message)
      embed=discord.Embed(title=" ", description=" ", color=0xdb781e)
      embed.set_footer(text='developer: Prisa')
      embed.set_author(name="Warn", icon_url=user.avatar_url)
      embed.set_image(url=" ")
      embed.add_field(name="User", value=" {} ".format(user.mention), inline=True)
      embed.add_field(name="Reason", value="{}".format(reason), inline=True)
      embed.add_field(name="Moderator", value=" {} ".format(ctx.message.author.mention), inline=True)
      await self.bot.send_message(discord.Object(id='528915422871945228'), embed=embed)
      
      await self.bot.send_message(user, "{} you was warned for {}".format(user.mention, reason))
      return
    else:
      return
    
def setup(bot):
  bot.add_cog(Moderation(bot))

