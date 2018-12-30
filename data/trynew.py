import discord
from discord.ext import commands

class Trynew:
  def __init__(self, bot):
    self.bot = bot 
                                
  async def on_member_join(self, member):
    if member.server.id == "528142547894272010":
      await self.bot.send_message(member, "👋Welcome👋 \n"
                                  "{} \n"
                                  "to **Join 4 Join** server \n"
                                  " \n"
                                  "to **verification**✅ your account write **.verify** in <#528209980734832642> \n"
                                  "read **information**📝 how to use **Join 4 Join** server and bot in <#528148347698020353>  \n"
                                  " \n"
                                  "If you need help with something, write **.help** \n"
                                  "or contact **Moderators**".format(member.mention))
      return
    elif member.server.id == "382204136990703616":
      server1 = self.bot.get_server("528142547894272010")
      if member in(server1.members):
        server = self.bot.get_server("528142547894272010")
        role = discord.utils.get(server.roles, id="528162784022626314")
        new_member = server.get_member(member.id)
        await self.bot.add_roles(new_member, role)
        await self.bot.send_message(discord.Object(id='528209980734832642'), "{} was verificate✅".format(member.mention))
 
    
def setup(bot):
  bot.add_cog(Trynew(bot))
