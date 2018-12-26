import discord
from discord.ext import commands

class Swearwords:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.author.bot: return
      
    if 'fuck' message.content:
      await self.bot.delete_message(message)
      embed = discord.Embed(title = '', description = '', colour = discord.Colour.orange())
      embed.set_footer(text='bot developer: Prisa#4835')
      embed.set_thumbnail(url='')
      embed.set_image(url='')
      embed.set_author(name='Warn', icon_url=message.author.avatar_url)
      embed.add_field(name='User', value= '{}'.format(message.author.mention), inline=True)
      embed.add_field(name='Reason', value='Swear Words ', inline=True)
      await self.bot.send_message(message.channel, embed=embed)
      
      
def setup(bot):
  bot.add_cog(Swearwords(bot))

