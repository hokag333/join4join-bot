import discord
from discord.ext import commands

class Moderation:
  def __init__(self, bot):
    self.bot = bot
  
  async def on_message(self, message):
    if message.author.bot:
      return
    if "528142547894272010" in(message.server.id):
      if "528148608533528596" in(message.channel.id):
        if message.content.startswith('!invites'):
          return
        else:
          await self.bot.delete_message(message)
          
      if "528209980734832642" in(message.channel.id):
        await self.bot.delete_message(message)
        
      if ('discord.gg') in message.content:
        if "528162784022626314" in(role.id for role in message.author.roles):
          return
        else:
          await self.bot.delete_message(message)
          embed=discord.Embed(title="__Warn__", description=" ", color=0x21ae09)
          embed.set_footer(text='developer: Prisa')
          embed.set_author(name=" ")
          embed.set_image(url=" ")
          embed.add_field(name="User", value=" {} ".format(message.author.mention), inline=True)
          await self.bot.send_message(discord.Object(id='528915422871945228'), embed=embed)
          await self.bot.send_message(message.channel, " {} you need have **verification account**, \n"
                                      "write **.verify** to make verification".format(message.author.mention))
    
def setup(bot):
  bot.add_cog(Moderation(bot))

