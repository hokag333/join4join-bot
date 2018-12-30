import discord
from discord.ext import commands

class Join:
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
    elif member.server.id == "382204136990703616":
      server1 = self.bot.get_server("528142547894272010")
      if member in(server1.members):
        await self.bot.send_message(discord.Object(id='528146368464945152'), "{} give Verify role pls".format(member.mention))
        await self.bot.send_message(discord.Object(id='528209980734832642'), "{} was verificate✅".format(member.mention))
        await self.bot.send_message(member, "{} \n"
                                    "Your account was verificate✅".format(member.mention))
        
  async def on_member_remove(self, member):
    if member.server.id == "382204136990703616":
      server1 = self.bot.get_server("528142547894272010")
      if member in(server1.members):
        await self.bot.send_message(member, "Verification error❌ \n"
                                    "{} \n"
                                    "You don´t meet the verification request \n"
                                    "try verify your account again".format(member.mention))
 
    
def setup(bot):
  bot.add_cog(Join(bot))
