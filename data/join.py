import discord
from discord.ext import commands

class Join:
  def __init__(self, bot):
    self.bot = bot 
                                
  async def on_member_join(self, member):
    if member.server.id("528142547894272010"):
      await self.bot.send_message(member, "{} \n"
                                  "👋Welcome👋 \n"
                                  "to **Join 4 Join** server \n"
                                  " \n"
                                  "write **.verify** in <#528209980734832642> to verification✅ your account \n"
                                  "check <#528148347698020353> and read 📝information how to use **Join 4 Join** server and bot \n"
                                  " \n"
                                  "If you need help with something, write **.help** \n"
                                  "or contact <@&528200802863677450>".format(member.mention))
      
    if member.server.id("458341394524798976"):
      server1 = self.bot.get_server("528142547894272010")
      if member in(server1):
        await self.bot.send_message(member, "{} \n"
                                    " Your account was verificate✅".format(member.mention))
      else:
        await self.bot.send_message(member, "test error")

    
  async def on_member_remove(self, member):
    if "382204136990703616" in(member.server.id):
      server1 = self.bot.get_server("528142547894272010")
      if member in(server1):
        await self.bot.send_message(member, "{} \n"
                                    "Verification error, bot can´t find you in **Chicken Server** members".format(member.mention))
    
def setup(bot):
  bot.add_cog(Join(bot))
