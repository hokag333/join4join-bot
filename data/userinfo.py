import discord
from discord.ext import commands

class Userinfo:
  def __init__(self, bot):
    self.bot = bot
    
    
  @commands.command(pass_context=True)
  async def me(self, ctx):
    embed=discord.Embed(title=" ", description="{}".format(ctx.message.author.name), color=0xfed83d)
    embed.set_author(name=" ")
    embed.set_image(url=ctx.message.author.avatar_url)
    if "Tier I" in(role.name for roles in ctx.message.author.role):
      embed.add_field(name="Tier", value="Tier I", inline=True)
    await self.bot.send_message(ctx.message.channel, embed=embed)
    
    
def setup(bot):
  bot.add_cog(Userinfo(bot))
