import discord
from discord.ext import commands

class Helper:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.author.bot: return
    
    
    if ('.help') in message.content:
      embed = discord.Embed(title = 'Help', description = '', colour = discord.Colour.blue())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='')
      embed.set_author(name='', icon_url='')
      embed.add_field(name='.cmds', value= 'all commands of bot', inline=True)
      embed.add_field(name='.responses', value= 'all chatting cmds to get  bot responses', inline=True)
      await self.bot.send_message(message.channel, embed=embed)
      
      
  @commands.command()
  async def bro(self):
    await self.bot.say('ring')
    
    
def setup(bot):
  bot.add_cog(Helper(bot))
