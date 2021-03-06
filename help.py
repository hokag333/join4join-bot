import discord
from discord.ext import commands

class Helper:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.author.bot: return
      
    if message.content.startswith('.mod'):
      if "537913297052106762" in(role.id for role in ctx.message.author.roles):
        mod = "537913297052106762"
      if "537913808975429642" in(role.id for role in ctx.message.author.roles):
        mod = "537913808975429642"
      if mod in(role.id for role in ctx.message.author.roles):
        embed = discord.Embed(title = '**__Help__**', description = 'moderator commands', colour = discord.Colour.blue())
        embed.set_footer(text='developer: Prisa#4835')
        embed.set_thumbnail(url='')
        embed.set_image(url='')
        embed.set_author(name='', icon_url='')
        embed.add_field(name='**warn**', value= 'to warn user', inline=True)
        embed.add_field(name='**clear**', value= 'clear messages (max 100)', inline=False)
        await self.bot.send_message(message.channel, embed=embed)
        return
      else:
        embed = discord.Embed(title = '**__Help__**', description = 'moderator commands', colour = discord.Colour.blue())
        embed.set_footer(text='developer: Prisa#4835')
        embed.set_thumbnail(url='')
        embed.set_image(url='')
        embed.set_author(name='', icon_url='')
        embed.add_field(name='** **', value= '** You are not moderator', inline=True)
        await self.bot.send_message(message.channel, embed=embed)
      
    if message.content.startswith('.cmds'):
      embed = discord.Embed(title = '**__Help__**', description = 'commands', colour = discord.Colour.blue())
      embed.set_footer(text='developer: Prisa#4835')
      embed.set_thumbnail(url='')
      embed.set_image(url='')
      embed.set_author(name='', icon_url='')
      embed.add_field(name='**.verify**', value= 'verify your account', inline=True)
      embed.add_field(name='**.report**', value= 'report user', inline=False)
      embed.add_field(name='**.userinfo**', value= 'info about user', inline=False)
      embed.add_field(name='**.dm**', value= 'dm invite links to some users **(need 20 invites)**', inline=False)
      await self.bot.send_message(message.channel, embed=embed)
      return
    
    if message.content.startswith('.bonus info'):
      embed = discord.Embed(title = '**__Bonuses__**', description = ' ', colour = discord.Colour.blue())
      embed.set_footer(text='developer: Prisa#4835')
      embed.set_thumbnail(url='')
      embed.set_image(url='')
      embed.set_author(name='', icon_url='')
      embed.add_field(name='**10 invites:**', value= 'can mention everyone', inline=True)
      embed.add_field(name='**20 invites:**', value= '1 per 24 hours can dm 10 random members by bot', inline=False)
      await self.bot.send_message(message.channel, embed=embed)
      return
      
    if message.content.startswith('.help'):
      embed = discord.Embed(title = '**__Help__**', description = '', colour = discord.Colour.blue())
      embed.set_footer(text='developer: Prisa#4835')
      embed.set_thumbnail(url='')
      embed.set_image(url='')
      embed.set_author(name='', icon_url='')
      embed.add_field(name='**.cmds**', value= 'commands', inline=True)
      embed.add_field(name='**.mod**', value= 'moderator commands', inline=False)
      embed.add_field(name='**.partnership**', value= 'info about **join4join** server partnership', inline=False)
      embed.add_field(name='**.bonus info**', value = 'bonuses which you can get', inline=False)
      embed.add_field(name='** **', value= '[chicken server](https://discord.gg/9hjAVpP)', inline=False)
      await self.bot.send_message(message.channel, embed=embed)
 
      
  @commands.command()
  async def ping(self):
    await self.bot.say('pong')
    
    
def setup(bot):
  bot.add_cog(Helper(bot))
