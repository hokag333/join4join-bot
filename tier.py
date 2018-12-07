import discord
from discord.ext import commands

class Tier:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.author.bot: return
      
    if message.content.startswith('none'):
      await self.bot.send_message(message.channel, 'new Class tested')
      
      
  @commands.command(pass_context=True)
  async def mytier(self, ctx, user: discord.User):
    if '508606486864461824' in (role.id for role in user.roles):
      await self.bot.send_message(message.channel, ' **{}** \n'
                                  'You have: **Tier X** '.format(user.name))
        
        
def setup(bot):
  bot.add_cog(Tier(bot))
