import discord
from discord.ext import commands

class Join:
  def __init__(self, bot):
    self.bot = bot 
                                
  async def on_member_join(self, member):
    await self.bot.send_message(member, "Hello {} \n"
                                "👋Welcome👋 to **Join 4 Join** server \n"
                                " \n"
                                "write **.verify** in <#528209980734832642> to verification✅ your account \n"
                                "check <#528148347698020353> and read 📝information📝 how to use **Join 4 Join** server and bot
                                "If you need help with something write **.help** in <#528147248706486282> \n"
                                "or contact <@&528200802863677450>".format(member.mention)
    
    
def setup(bot):
  bot.add_cog(Join(bot))
