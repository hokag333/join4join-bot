import discord
from discord.ext import commands

class Join:
  def __init__(self, bot):
    self.bot = bot 
                                
  async def on_member_join(self, member):
    chickenserver = self.bot.get_server("382204136990703616")
    join4joinserver = self.bot.get_server("382204136990703616")
    if "382204136990703616" in(server):
      if member in(join4joinserver.members):
        await self.bot.send_message(member, "You was verificate your account")
        return
      else:
        return
    if server in(join4joinserver):
      await self.bot.send_message(member, "Hello {} \n"
                                  "👋Welcome👋 to \n"
                                  "**Join 4 Join** server \n"
                                  " \n"
                                  "write **.verify** in <#528209980734832642> to verification✅ your account \n"
                                  "check <#528148347698020353> and read 📝information📝 how to use **Join 4 Join** server and bot \n"
                                  " \n"
                                  "If you need help with something, write **.help** in <#528147248706486282> \n"
                                  "or contact <@&528200802863677450>".format(member.mention)
    
    
def setup(bot):
  bot.add_cog(Join(bot))
