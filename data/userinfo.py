import discord
from discord.ext import commands

class Userinfo:
  def __init__(self, bot):
    self.bot = bot
    
    
  @commands.command(pass_context=True)
  async def userinfo(self, ctx, user: discord.User=None):
    if not user:
      user = ctx.message.author
    tierid = "not" 
    if "520630368668483594" in(role.id for role in user.roles):
      tierid = "Tier I" 
    embed=discord.Embed(title="User", description="{}".format(user.name), color=0xfed83d)
    embed.set_author(name=" ")
    embed.set_image(url=user.avatar_url)
    embed.add_field(name="Highest role", value=" {} ".format(user.top_role.mention), inline=True)
    embed.add_field(name="Tier", value=" {} ".format(tierid), inline=True) 
    await self.bot.send_message(ctx.message.channel, embed=embed)
    
    
def setup(bot):
  bot.add_cog(Userinfo(bot))
