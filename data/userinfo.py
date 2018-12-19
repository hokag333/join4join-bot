import discord
from discord.ext import commands

class Userinfo:
  def __init__(self, bot):
    self.bot = bot
    
    
  @commands.command(pass_context=True)
  async def userinfo(self, ctx, user: discord.User=None):
    if not user:
      user = ctx.message.author
    #Diamond Tiers
    if "520631199710969864" in(role.id for role in user.roles):
      tierid = "<@&520631199710969864>"
    if "" in(role.id for role in user.roles):
      tierid = "<@&520631201778892810>"
    if "520631013748113418" in(role.id for role in user.roles):
      tierid = "<@&520631013748113418>"
    if "520631017376186388" in(role.id for role in user.roles):
      tierid = "<@&520631017376186388>"
    if "520631021125763082" in(role.id for role in user.roles):
      tierid = "<@&520631021125763082>"
    if "520630751897583626" in(role.id for role in user.roles):
      tierid = "<@&520630751897583626>"
    if "520630661678235648" in(role.id for role in user.roles):
      tierid = "<@&520630661678235648>"
    if "520630586369507350" in(role.id for role in user.roles):
      tierid = "<@&520630586369507350>"
    if "520630502827229184" in(role.id for role in user.roles):
      tierid = "<@&520630502827229184>"
    if "520630368668483594" in(role.id for role in user.roles):
      tierid = "<@&520630368668483594>"
    #Platinum Tiers
    if "520632449898774550" in(role.id for role in user.roles):
      tierid = "<@&520632449898774550>"
    if "520632455305232384" in(role.id for role in user.roles):
      tierid = "<@&520632455305232384>"
    if "520632457930997770" in(role.id for role in user.roles):
      tierid = "<@&520632457930997770>"
    if "520632460422283290" in(role.id for role in user.roles):
      tierid = "<@&520632460422283290>"
    if "520632462351663109" in(role.id for role in user.roles):
      tierid = "<@&520632462351663109>"
    if "520632464323117056" in(role.id for role in user.roles):
      tierid = "<@&520632464323117056>"
    if "520632466311086090" in(role.id for role in user.roles):
      tierid = "<@&520632466311086090>"
    if "520632468328415233" in(role.id for role in user.roles):
      tierid = "<@&520632468328415233>"
    if "520632470253862912" in(role.id for role in user.roles):
      tierid = "<@&520632470253862912>"
    if "520632473583878164" in(role.id for role in user.roles):
      tierid = "<@&520632473583878164>"
    #Normal Tiers
    if "508606486864461824" in(role.id for role in user.roles):
      tierid = "<@&508606486864461824>"
    if "508606351493169155" in(role.id for role in user.roles):
      tierid = "<@&508606351493169155>"
    if "508606276666654720" in(role.id for role in user.roles):
      tierid = "<@&508606276666654720>"
    if "508606197461680138" in(role.id for role in user.roles):
      tierid = "<@&508606197461680138>"
    if "508606126497988609" in(role.id for role in user.roles):
      tierid = "<@&508606126497988609>"
    if "508606074736214036" in(role.id for role in user.roles):
      tierid = "<@&508606074736214036>"
    if "508605954875719698" in(role.id for role in user.roles):
      tierid = "<@&508605954875719698>"
    if "508605725874978825" in(role.id for role in user.roles):
      tierid = "<@&508605725874978825>"
    if "508605659143471104" in(role.id for role in user.roles):
      tierid = "<@&508605659143471104>"
    if "508605450770448384" in(role.id for role in user.roles):
      tierid = "<@&508605450770448384>"
    else:
      tierid = "none" 
    embed=discord.Embed(title="User", description="{}".format(user.name), color=0xfed83d)
    embed.set_author(name=" ")
    embed.set_image(url=user.avatar_url)
    embed.add_field(name="Highest role", value=" {} ".format(user.top_role.mention), inline=True)
    embed.add_field(name="Tier", value=" {} ".format(tierid), inline=True)
    embed.add_field(name="Join at", value=" {} ".format(user.joined_at), inline=False)
    await self.bot.send_message(ctx.message.channel, embed=embed)
    
    
def setup(bot):
  bot.add_cog(Userinfo(bot))
