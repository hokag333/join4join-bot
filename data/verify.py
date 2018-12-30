import discord
from discord.ext import commands

class Verify:
  def __init__(self, bot):
    self.bot = bot
    
  async def on_command_error(self, error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
      message = content="You have %.5s s cooldown on this command" % error.retry_after
      await self.bot.send_message(ctx.message.channel, message)
      raise error
    
  @commands.command(pass_context=True)
  async def verify(self, ctx):
    if "528142547894272010" in (ctx.message.server.id):
      await self.bot.send_message(ctx.message.author, "{} just confirm your Verification".format(ctx.message.author.mention))
      await self.bot.delete_message(ctx.message)
      embed = discord.Embed(title = '', description = '', colour = discord.Colour.orange())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='')
      embed.set_author(name='', icon_url='')
      embed.add_field(name='to verify your account', value= '[click here](https://discord.gg/9hjAVpP)', inline=True)
      await self.bot.send_message(ctx.message.author, embed=embed)
      first_message_var = await self.bot.send_message(self.bot.get_channel('528209980734832642'), "Procesing ...")
      await self.bot.edit_message(first_message_var, " {} waiting for verification🌀".format(ctx.message.author.mention))
    
  @commands.command(pass_context=True)
  async def verified(self, ctx, user: discord.User):
    if "528142547894272010" in (ctx.message.server.id):
      if "528145435022327810" in(role.id for role in ctx.message.author.roles):
        await self.bot.add_roles(member, get_role(self.bot.get_server("528142547894272010").roles.id('528162784022626314')
        await self.bot.send_message(user, "{} \n"
                                    "Your account was verificate✅ \n"
                                    "**invite links** in **Join 4 Join** server is enabled ".format(user.mention))
        await self.bot.send_message(self.bot.get_channel('528209980734832642'), "{} was verificate✅".format(user.mention))
        return
      await self.bot.delete_message(ctx.message)
    
  @commands.command(pass_context=True)
  async def verifyerror(self, ctx, user: discord.User):
    if "528142547894272010" in (ctx.message.server.id):
      if "528145435022327810" in(role.id for role in ctx.message.author.roles):
        await self.bot.send_message(user, "❗verification error❗ \n"
                                    "{} you are not **Chicken Server** member \n"
                                    "If you want to get **verification** and enable post **invite links** \n"
                                    " \n"
                                    "Join **Chicken Server** \n"
                                    "https://discord.gg/9hjAVpP".format(user.mention))
        await self.bot.send_message(ctx.message.channel, "{} get verification error message".format(user.mention))
        return
      await self.bot.delete_message(ctx.message)
    
def setup(bot):
  bot.add_cog(Verify(bot))
