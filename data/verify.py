import discord
from discord.ext import commands

class Verify:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(pass_context=True)
  async def verify(self, ctx):
    if "528142547894272010" in (ctx.message.server.id):
      await self.bot.delete_message(ctx.message)
      await self.bot.send_message(ctx.message.author, "{}".format(ctx.message.author.mention))
      
      embed = discord.Embed(title = '🔄__Verification__', description = ' ', colour = discord.Colour.orange())
      embed.set_footer(text=' ')
      embed.set_thumbnail(url=' ')
      embed.set_image(url=' ')
      embed.set_author(name=' ', icon_url=' ')
      embed.add_field(name='just confirm verification', value= '[click here](https://discord.gg/9hjAVpP)', inline=True)
      await self.bot.send_message(ctx.message.author, embed=embed)
      
      embed=discord.Embed(title="🔄__Verification__", description=" ", color=0x1378ca)
      embed.set_footer(text='Processing ...')
      embed.set_author(name=" ")
      embed.set_image(url=" ")
      embed.add_field(name="User", value=" {} ".format(ctx.message.author.mention), inline=True)
      await self.bot.send_message(discord.Object(id='529194384764174337'), embed=embed)
    
def setup(bot):
  bot.add_cog(Verify(bot))
