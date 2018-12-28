import discord
from discord.ext import commands

class Helper:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.author.bot: return
    
    
    if message.content.startswith('.help'):
      embed = discord.Embed(title = 'Help', description = '', colour = discord.Colour.blue())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='')
      embed.set_author(name='', icon_url='')
      embed.add_field(name='** **', value= '[chicken server](https://discord.gg/9hjAVpP)', inline=True)
      embed.add_field(name='** **', value= '[chicken website](http://chickenserver.wix.com/website)', inline=True)
      await self.bot.send_message(message.channel, embed=embed)
      
      
      
      
  @commands.command()
  async def ping(self):
    await self.bot.say('pong')
    
    
def setup(bot):
  bot.add_cog(Helper(bot))
