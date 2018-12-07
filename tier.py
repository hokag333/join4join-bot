import discord
from discord.ext import commands

class Tier:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.author.bot: return
      
    if message.content.startswith('testtiercmd'):
      await self.bot.send_message(message.channel, ' **{}** \n'
                                  'You have: **Tier X** '.format(message.author.name))
      
  @commands.command(pass_context=True)
  async def Tier(self, ctx, user: discord.User=None):
    if not user:
      #mentioned user Tiers
      #Platinum Tiers
      if "520632449898774550" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Platinum Tier X** ".format(ctx.message.author.name))
        return
      if "520632455305232384" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Platinum Tier IX** ".format(ctx.message.author.name))
        return
      if "520632457930997770" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Platinum Tier VIII** ".format(ctx.message.author.name))
        return
      if "520632460422283290" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Platinum Tier VII** ".format(ctx.message.author.name))
        return
      if "520632462351663109" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Platinum Tier VI** ".format(ctx.message.author.name))
        return
      if "520632464323117056" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Platinum Tier V** ".format(ctx.message.author.name))
        return
      if "520632466311086090" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Platinum Tier IV** ".format(ctx.message.author.name))
        return
      if "520632468328415233" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Platinum Tier III** ".format(ctx.message.author.name))
        return
      if "520632470253862912" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Platinum Tier II** ".format(ctx.message.author.name))
        return
      if "520632473583878164" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Platinum Tier I** ".format(ctx.message.author.name))
      #Normal Tiers
      if "508606486864461824" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Tier X** ".format(ctx.message.author.name))
        return
      if "508606351493169155" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Tier IX** ".format(ctx.message.author.name))
        return
      if "508606276666654720" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Tier VIII** ".format(ctx.message.author.name))
        return
      if "508606197461680138" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Tier VII** ".format(ctx.message.author.name))
        return
      if "508606126497988609" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Tier VI** ".format(ctx.message.author.name))
        return
      if "508606074736214036" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Tier V** ".format(ctx.message.author.name))
        return
      if "508605954875719698" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Tier IV** ".format(ctx.message.author.name))
        return
      if "508605725874978825" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Tier III** ".format(ctx.message.author.name))
        return
      if "508605659143471104" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Tier II** ".format(ctx.message.author.name))
        return
      if "508605450770448384" in (role.id for role in ctx.message.author.roles):
        await self.bot.say(" **{}** \n"
                           "You have: **Tier I** ".format(ctx.message.author.name))
        return
      else:
        await self.bot.say(" **{}** \n"
                           "You haven´t got any Tier".format(ctx.message.author.name))
    else:
      #mentioned user Tiers
      #Platinum Tiers
      if "520632449898774550" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Platinum Tier X** ".format(user.name))
        return
      if "520632455305232384" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Platinum Tier IX** ".format(user.name))
        return
      if "520632457930997770" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Platinum Tier VIII** ".format(user.name))
        return
      if "520632460422283290" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Platinum Tier VII** ".format(user.name))
        return
      if "520632462351663109" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Platinum Tier VI** ".format(user.name))
        return
      if "520632464323117056" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Platinum Tier V** ".format(user.name))
        return
      if "520632466311086090" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Platinum Tier IV** ".format(user.name))
        return
      if "520632468328415233" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Platinum Tier III** ".format(user.name))
        return
      if "520632470253862912" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Platinum Tier II** ".format(user.name))
        return
      if "520632473583878164" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Platinum Tier I** ".format(user.name))
      #Normal Tiers
      if "508606486864461824" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Tier X** ".format(user.name))
        return
      if "508606351493169155" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Tier IX** ".format(user.name))
        return
      if "508606276666654720" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Tier VIII** ".format(user.name))
        return
      if "508606197461680138" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Tier VII** ".format(user.name))
        return
      if "508606126497988609" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Tier VI** ".format(user.name))
        return
      if "508606074736214036" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Tier V** ".format(user.name))
        return
      if "508605954875719698" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Tier IV** ".format(user.name))
        return
      if "508605725874978825" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Tier III** ".format(user.name))
        return
      if "508605659143471104" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Tier II** ".format(user.name))
        return
      if "508605450770448384" in (role.id for role in user.roles):
        await self.bot.say(" **{}** \n"
                           "have: **Tier I** ".format(user.name))
        return
      else:
        await self.bot.say(" **{}** \n"
                           "haven´t got any Tier".format(user.name))
        
        
def setup(bot):
  bot.add_cog(Tier(bot))
