import discord
from discord.ext import commands

class Tier:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.author.bot: return
      
    if message.content.startswith('!Tier'):
      if '508606486864461824' in (role.id for role in message.author.roles):
        await self.bot.send_message(message.channel, ' **{}** \n'
                                    'You have: **Tier X** '.format(message.author.name))
        return
      if '508606351493169155' in (role.id for role in message.author.roles):
        await self.bot.send_message(message.channel, ' **{}** \n'
                                    'You have: **Tier IX** '.format(message.author.name))
        return
      if '508606276666654720' in (role.id for role in message.author.roles):
        await self.bot.send_message(message.channel, ' **{}** \n'
                                    'You have: **Tier VIII** '.format(message.author.name))
        return
      if '508606197461680138' in (role.id for role in message.author.roles):
        await self.bot.send_message(message.channel, ' **{}** \n'
                                    'You have: **Tier VII** '.format(message.author.name))
        return
      if '508606126497988609' in (role.id for role in message.author.roles):
        await self.bot.send_message(message.channel, ' **{}** \n'
                                    'You have: **Tier VI** '.format(message.author.name))
        return
      if '508606074736214036' in (role.id for role in message.author.roles):
        await self.bot.send_message(message.channel, ' **{}** \n'
                                    'You have: **Tier V** '.format(message.author.name))
        return
      if '508605954875719698' in (role.id for role in message.author.roles):
        await self.bot.send_message(message.channel, ' **{}** \n'
                                    'You have: **Tier IV** '.format(message.author.name))
        return
      if '508605725874978825' in (role.id for role in message.author.roles):
        await self.bot.send_message(message.channel, ' **{}** \n'
                                    'You have: **Tier III** '.format(message.author.name))
        return
      if '508605659143471104' in (role.id for role in message.author.roles):
        await self.bot.send_message(message.channel, ' **{}** \n'
                                    'You have: **Tier II** '.format(message.author.name))
        return
      if '508605450770448384' in (role.id for role in message.author.roles):
        await self.bot.send_message(message.channel, ' **{}** \n'
                                    'You have: **Tier I** '.format(message.author.name))
        return
      else:
        await self.bot.send_message(message.channel, ' **{}** \n'
                                    'You have not any Tier'.format(message.author.name))
      
      
  @commands.command(pass_context=True)
  async def mytier(self, ctx, user: discord.User):
    if not user:
      if "508606486864461824" in (role.id for role in message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Tier X** ".format(message.author.roles))
    else:
      if "508606486864461824" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Tier X** ".format(user.name))
      else:
        await self.bot.say(" **{}** \n"
                           "You have not any Tier".format(user.name))
        
        
def setup(bot):
  bot.add_cog(Tier(bot))
