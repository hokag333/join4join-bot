import discord
from discord.ext import commands
from data import pointsdata

class Points:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.author.bot: return
    
    if message.content.startswith('trynewpoints'):
      await self.bot.send_message(message.channel, 'points comming soon')
      
      
  @commands.command(pass_context=True)
  async def give(self, ctx, member: discord.Member):
    points[member.id] += 1
    await self.bot.say("{} now has {} points".format(member.mention, points[member.id]))
    
  @commands.command(pass_context=True)
  async def points(self, ctx, member: discord.Member):
    await self.bot.say("{} has {} points".format(member.mention, points[member.id]))
    

def setup(bot):
  bot.add_cog(Points(bot))
