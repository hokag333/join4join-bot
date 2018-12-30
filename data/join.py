import discord
from discord.ext import commands

class Join:
  def __init__(self, bot):
    self.bot = bot 
                                
  async def on_member_join(self, member, server: discord.Server):
    if member_join(server.id("528142547894272010")):
      await self.bot.send_message(member, "test message")
      return
    server1 = self.bot.get_server("528142547894272010")
    if member in(server1):
      server2 = self.bot.get_server("382204136990703616")
      if member in(server2.members):
        await self.bot.send_message(member, "{} \n"
                                    " Your account was verificate✅".format(member.mention))
        return
      server1 = self.bot.get_server("528142547894272010")
      if member in(server1):
        await self.bot.send_message(member, "{} \n"
                                    "👋Welcome👋 to \n"
                                    "**    ** **Join 4 Join** server \n"
                                    " \n"
                                    "write **.verify** in <#528209980734832642> to verification✅ your account \n"
                                    "check <#528148347698020353> and read 📝information how to use **Join 4 Join** server and bot \n"
                                    " \n"
                                    "If you need help with something, write **.help** in <#528147248706486282> \n"
                                    "or contact <@&528200802863677450>".format(member.mention))

    
  async def on_member_remove(self, member):
    server2 = self.bot.get_server("528142547894272010")
    if member (server2.members):
      server1 = self.bot.get_server("382204136990703616")
      if member in(server1.members):
        return
      else:
        server2 = self.bot.get_server("528142547894272010")
        if "528162784022626314" in(role.id for role in member.roles in server2):
          await self.bot.send_message(member, "{} Your account **Verification error** \n"
                                      "You was maybe left **Chicken Server** \n"
                                      "If you want to **Verificate** your account write **.verify**".format(member.mention))
          return
    
def setup(bot):
  bot.add_cog(Join(bot))
