import discord
from discord.ext import commands

class Level:
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(pass_context=True)
  async def casino(self, ctx, reason):
    if "on" in(reason): 
      await self.bot.send("casino is open")
    if "off" in(reason):
      await self.bot.send("casino is closed")
    
  async def on_message(self, message):
    casinoch = "506512907786518528" in(message.channel.id)
    if not casinoch:
      return
    if message.content.startswith('open box 1'):
      await self.bot.send_message(message.channel, "nothing in box")
    
def setup(bot):
  bot.add_cog(Level(bot))
