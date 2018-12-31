import discord
from discord.ext import commands

class Trynew:
  def __init__(self, bot):
    self.bot = bot 
                                
  async def on_member_join(self, member):
    if member.server.id == "528142547894272010":
      server = self.bot.get_server("528142547894272010")
      role = discord.utils.get(server.roles, id="529027718340280327")
      new_member = server.get_member(member.id)
      await self.bot.add_roles(new_member, role)
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
        await self.bot.send_message(member, "{} \n"
                                    "Your account was verificate✅ \n"
                                    "You can now post **invite links** in **Join 4 Join** server".format(member.mention))
        
        embed=discord.Embed(title="✅__Verification__", description=" ", color=0x2be20a)
        embed.set_footer(text='verificate')
        embed.set_author(name=" ")
        embed.set_image(url=" ")
        embed.add_field(name="User", value=" {} ".format(member.mention), inline=True)
        await self.bot.send_message(discord.Object(id='529194384764174337'), embed=embed)
        return
      
  async def on_member_remove(self, member):
    if member.server.id == "382204136990703616":
      server1 = self.bot.get_server("528142547894272010")
      if member in(server1.members):
        server = self.bot.get_server("528142547894272010")
        role = discord.utils.get(server.roles, id="528162784022626314")
        left_member = server.get_member(member.id)
        await self.bot.remove_roles(left_member, role)
        await self.bot.send_message(discord.Object(id='528915422871945228'), "{} **Verification error**❌ check if role was removed".format(member.mention))
        await self.bot.send_message(member, "**Verification error**❌ \n"
                                    "{} \n"
                                    "You don´t meet the verification request \n"
                                    "try **verify** your account again".format(member.mention))
        
        embed=discord.Embed(title="❌__Verification__", description=" ", color=0x2be20a)
        embed.set_footer(text='error')
        embed.set_author(name=" ")
        embed.set_image(url=" ")
        embed.add_field(name="User", value=" {} ".format(member.mention), inline=True)
        await self.bot.send_message(discord.Object(id='529194384764174337'), embed=embed)
        return
 
    
def setup(bot):
  bot.add_cog(Trynew(bot))
