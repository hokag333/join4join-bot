import discord
from discord.ext import commands

class Verify:
  def __init__(self, bot):
    self.bot = bot 
                                
  async def on_member_join(self, member):
    if member.server.id == "537014667550261318":
      server = self.bot.get_server("537014667550261318")
      role = discord.utils.get(server.roles, id="537913978479837194")
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
      
      await self.bot.send_message(discord.Object(id='537918427059453952'), "{} joined **Join 4 Join** server✅ \n account created at** {} ** ".format(member.mention, user.joined_at.strftime(" %d %B %Y ")))
      return
    elif member.server.id == "537014489598394399":
      server1 = self.bot.get_server("537014667550261318")
      if member in(server1.members):
        server = self.bot.get_server("537014667550261318")
        role = discord.utils.get(server.roles, id="537914257639997441")
        new_member = server.get_member(member.id)
        await self.bot.add_roles(new_member, role)
        await self.bot.send_message(discord.Object(id='537921215168512000'), "{} was verified✅".format(member.mention))
        await self.bot.send_message(member, "{} \n"
                                    "Your account was verified✅ \n"
                                    "You can now post **invite links** in **Join 4 Join** server".format(member.mention))
        
        embed=discord.Embed(title="✅__Verification__", description=" ", color=0x21ae09)
        embed.set_footer(text='verified')
        embed.set_author(name=" ")
        embed.set_image(url=" ")
        embed.add_field(name="User", value=" {} ".format(member.mention), inline=True)
        await self.bot.send_message(discord.Object(id='539070627517038612'), embed=embed)
        return
      
  async def on_member_remove(self, member):
    if member.server.id == "537014489598394399":
      server1 = self.bot.get_server("537014667550261318")
      if member in(server1.members):
        server = self.bot.get_server("537014667550261318")
        role = discord.utils.get(server.roles, id="537914257639997441")
        left_member = server.get_member(member.id)
        await self.bot.remove_roles(left_member, role)
        await self.bot.send_message(member, "**Verification error**❌ \n"
                                    "{} \n"
                                    "You are not satisfy request for verification \n"
                                    "try **verify** your account again".format(member.mention))
        
        embed=discord.Embed(title="❌__Verification__", description=" ", color=0xc11515)
        embed.set_footer(text='error')
        embed.set_author(name=" ")
        embed.set_image(url=" ")
        embed.add_field(name="User", value=" {} ".format(member.mention), inline=True)
        await self.bot.send_message(discord.Object(id='539070627517038612'), embed=embed)
        return
      else:
        return
      
    elif member.server.id == "537014667550261318":
      await self.bot.send_message(discord.Object(id='537918427059453952'), "{} left **Join 4 Join** server🔴".format(member.mention))
    else:
      return
      
  @commands.command(pass_context=True)
  async def verify(self, ctx):
    if "537014667550261318" in(ctx.message.server.id):
      if "537914257639997441" in(role.id for role in ctx.message.author.roles):
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.author, "You already have a verified✅ account")
        return
      
      server2 = self.bot.get_server("537014489598394399")
      if ctx.message.author in(server2.members):
        server = self.bot.get_server("537014667550261318")
        role = discord.utils.get(server.roles, id="537914257639997441")
        member = server.get_member(ctx.message.author.id)
        await self.bot.delete_message(ctx.message)
        await self.bot.add_roles(member, role)
        await self.bot.send_message(discord.Object(id='537921215168512000'), "{} was verified✅".format(ctx.message.author.mention))
        await self.bot.send_message(ctx.message.author, "{} \n"
                                    "Your account was verified✅ \n"
                                    "You can now post **invite links** in **Join 4 Join** server".format(ctx.message.author.mention))
        
        embed=discord.Embed(title="✅__Verification__", description=" ", color=0x21ae09)
        embed.set_footer(text='verified')
        embed.set_author(name=" ")
        embed.set_image(url=" ")
        embed.add_field(name="User", value=" {} ".format(ctx.message.author.mention), inline=True)
        await self.bot.send_message(discord.Object(id='539070627517038612'), embed=embed)
        return
      
      await self.bot.delete_message(ctx.message)
      await self.bot.send_message(ctx.message.author, "{}".format(ctx.message.author.mention))
      
      embed = discord.Embed(title = '🔄__Verification__', description = ' ', color=0x1378ca)
      embed.set_footer(text=' ')
      embed.set_thumbnail(url=' ')
      embed.set_image(url=' ')
      embed.set_author(name=' ', icon_url=' ')
      embed.add_field(name='just confirm verification', value= '[click here](https://discord.gg/ZSNcHxu)', inline=True)
      await self.bot.send_message(ctx.message.author, embed=embed)
      
      embed=discord.Embed(title="🔄__Verification__", description=" ", color=0x1378ca)
      embed.set_footer(text='Processing ...')
      embed.set_author(name=" ")
      embed.set_image(url=" ")
      embed.add_field(name="User", value=" {} ".format(ctx.message.author.mention), inline=True)
      await self.bot.send_message(discord.Object(id='539070627517038612'), embed=embed)
      return
    
 
    
def setup(bot):
  bot.add_cog(Verify(bot))
