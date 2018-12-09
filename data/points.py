import discord
from discord.ext import commands

class Points:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.author.bot: return
    
    if message.content.startswith('!points help'):
      await self.bot.send_message(message.channel, ' **{}**  to view your points write !points \n'.format(message.author.name))
      
  @commands.command(pass_context=True)
  async def points(self, ctx, user: discord.User=None):
    if not user:
      #Prisa#4835
      if "381887710308335618" in (ctx.message.author.id):
        await self.bot.say(" **{}** you have **∞** points".format(ctx.message.author.name))
        return
      else:
        await self.bot.say(" **{}** you don´t have any points \n"
                           "or isn´t write".format(ctx.message.author.name))
        
        
def setup(bot):
  bot.add_cog(Points(bot))
