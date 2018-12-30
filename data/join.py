import discord
from discord.ext import commands

class Join:
  def __init__(self, bot):
    self.bot = bot 
                                
  async def on_member_join(self, member):
    if member.server.id == "528142547894272010":
      role = self.bot.get_server.role("528200802863677450")
      await self.bot.send_message(member, "👋Welcome👋 \n"
                                  "{} \n"
                                  "to **Join 4 Join** server \n"
                                  " \n"
                                  "to **verification**✅ your account write **.verify** in <#528209980734832642> \n"
                                  "read **information**📝 how to use **Join 4 Join** server and bot in <#528148347698020353>  \n"
                                  " \n"
                                  "If you need help with something, write **.help** \n"
                                  "or contact {} ".format(member.mention, role.mention))
    elif member.server.id == "458341394524798976":
      server1 = self.bot.get_server("528142547894272010")
      if member in(server1.members):
        await self.bot.send_message(member, "{} \n"
                                    " Your account was verificate✅".format(member.mention))
 
    
def setup(bot):
  bot.add_cog(Join(bot))
