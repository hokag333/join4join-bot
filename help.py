import discord
from discord.ext import commands

class Helper:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.author.bot: return
      
    if message.content.startswith('.help mod'):
      embed = discord.Embed(title = 'Help', description = 'moderator commands', colour = discord.Colour.blue())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='')
      embed.set_author(name='', icon_url='')
      embed.add_field(name='verified', value= 'if user was verified, (joined Chicken Server)', inline=True)
      embed.add_field(name='verifyerror', value= 'if user wasn´t verified, (wasn´t joined Chicken Server)', inline=True)
      await self.bot.send_message(message.channel, embed=embed)
      return
      
    if message.content.startswith('.help cmds'):
      embed = discord.Embed(title = 'Help', description = 'moderator commands', colour = discord.Colour.blue())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='')
      embed.set_author(name='', icon_url='')
      embed.add_field(name='verify', value= 'verify your account', inline=True)
      embed.add_field(name='dm', value= 'dm invite links to all users (need 20 invites)', inline=True)
      await self.bot.send_message(message.channel, embed=embed)
      return
      
    if message.content.startswith('.help'):
      embed = discord.Embed(title = 'Help', description = '', colour = discord.Colour.blue())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='')
      embed.set_author(name='', icon_url='')
      embed.add_field(name='cmds', value= 'commands', inline=True)
      embed.add_field(name='mod', value= 'moderator commands', inline=True)
      embed.add_field(name='** **', value= '[chicken server](https://discord.gg/9hjAVpP)', inline=True)
      await self.bot.send_message(message.channel, embed=embed)
 
      
  @commands.command()
  async def ping(self):
    await self.bot.say('pong')
    
    
def setup(bot):
  bot.add_cog(Helper(bot))
