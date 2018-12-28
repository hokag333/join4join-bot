import discord
from discord.ext import commands

class Join:
  def __init__(self, bot):
    self.bot = bot 
                                
  async def on_member_join(self, member):
    await self.bot.send_message(member, "Hello {} \n"
                                "If you want to have permissions to post invite links on **Join 4 Join** server \n"
                                "go to the <#528209980734832642> and write **.verify** to verification your account".format(member.mention)
    
    
def setup(bot):
  bot.add_cog(Join(bot))
