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
      embed.add_field(name='.cmds', value= 'all commands of bot', inline=True)
      embed.add_field(name='.responses', value= 'all chatting cmds with bot responses', inline=True)
      await self.bot.send_message(message.channel, embed=embed)
      
    if message.content.startswith('.checktest'):
      embed = discord.Embed(title = 'Help', description = 'cmds', colour = discord.Colour.blue())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='')
      embed.set_author(name='', icon_url='')
      embed.add_field(name='!Tier @user_mention', value= 'show user´s **Tier**', inline=True)
      await self.bot.send_message(message.channel, embed=embed)
      
    if message.content.startswith('.cmds'):
      embed = discord.Embed(title = 'Help', description = 'cmds', colour = discord.Colour.blue())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='')
      embed.set_author(name='', icon_url='')
      embed.add_field(name='!Tier', value= 'show your **Tier**', inline=False)
      embed.add_field(name='!Tier @user_mention', value= 'show user´s **Tier**', inline=True)
      await self.bot.send_message(message.channel, embed=embed)
      
      
      
  @commands.command()
  async def bro(self):
    await self.bot.say('ring')
    
    
def setup(bot):
  bot.add_cog(Helper(bot))
