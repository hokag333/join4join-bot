import discord
from discord.ext import commands

class Join:
  def __init__(self, bot):
    self.bot = bot 
                                
  async def on_member_join(self, member):
    server1 = self.bot.get_server("382204136990703616")
    if member in(server1.members):
      server2 = self.bot.get_server("528142547894272010")
      if member in(server2.members):
        await self.bot.send_message(member, "{} Your account was verificate".format(member.mention))
        return
      else:
        return
    server2 = self.bot.get_server("528142547894272010")
    if member in(server2.members):
      await self.bot.send_message(member, "Hello {} \n"
                                  "👋Welcome👋 to \n"
                                  "**Join 4 Join** server \n"
                                  " \n"
                                  "write **.verify** in <#528209980734832642> to verification✅ your account \n"
                                  "check <#528148347698020353> and read 📝information📝 how to use **Join 4 Join** server and bot \n"
                                  " \n"
                                  "If you need help with something, write **.help** in <#528147248706486282> \n"
                                  "or contact <@&528200802863677450>".format(member.mention))
      return
    else:
      return
    
  async def on_member_remove(self, member):
    server1 = self.bot.get_server("382204136990703616")
    if member.remove in(server1.members):
      server2 = self.bot.get_server("528142547894272010")
      if member in(server2.members):
        await self.bot.send_message(member, "{} Verification error".format(member.mention))
        return
    else:
      return
    
def setup(bot):
  bot.add_cog(Join(bot))
