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
    embed.add_field(name="top role", value=" {} ".format(ctx.message.author.top_role.name), inline=True) 
    await self.bot.send_message(ctx.message.channel, embed=embed)
    
    
def setup(bot):
  bot.add_cog(Userinfo(bot))
