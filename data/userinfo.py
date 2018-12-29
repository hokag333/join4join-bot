import discord
from discord.ext import commands

class Userinfo:
  def __init__(self, bot):
    self.bot = bot 
                                
  @commands.command(pass_context=True)
  async def userinfo(self, ctx, user: discord.User=None):
    if not user:
      user = ctx.message.author
                                                                
    embed=discord.Embed(title="User", description="{}".format(user.mention), color=0xfed83d)
    embed.set_author(name=" ")
    embed.set_image(url=user.avatar_url)
    embed.add_field(name="Highest role", value=" {} ".format(user.top_role.mention), inline=True)
    embed.add_field(name="Joined at", value=" {} ".format(user.joined_at.strftime(" %d %B %Y ")), inline=False)
    embed.add_field(name="Account Created at", value=" {} ".format(user.created_at.strftime(" %d %B %Y ")), inline=False)
    await self.bot.send_message(ctx.message.channel, embed=embed)
    
  @commands.command(pass_context=True)
  async def testme(self, ctx):
    if "458341394524798976" in(server.id for server in ctx.message.author.server):
      await self.bot.send_message(ctx.message.channel, "{} test complete".format(ctx.message.author.mention))
    
    
def setup(bot):
  bot.add_cog(Userinfo(bot))
