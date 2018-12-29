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
  @commands.cooldown(1, 60*5, commands.BucketType.user)
  async def verify(self, ctx):
    await self.bot.delete_message(ctx.message)
    await self.bot.send_message(ctx.message.author, "**Chicken server** \n"
                                "🔄**Game Updates** - for new updates of games \n"
                                "🎥**Twitch bot** - for watching live streams on discord server \n"
                                "🎵**Music bots** - for listen songs with your friends \n"
                                "👌**memes** \n"
                                "🐻**funny animals** \n"
                                "🤔**would you rather** \n"
                                "🔔**selectable roles** - you can choose which you want to use and get notify on the server \n"
                                "❔**helper** - when you need help with something \n"
                                "📢**giveaways** - you can join on our website \n"
                                "💬**Chat Rooms** and 🔈**Voice Rooms** \n"
                                "and more \n"
                                " \n"
                                "**Invite** : {} **__to verification join this server__** \n"
                                "https://discord.gg/9hjAVpP".format(ctx.message.author.mention))
    first_message_var = await self.bot.send_message(self.bot.get_channel('528209980734832642'), "Procesing ...")
    await self.bot.edit_message(first_message_var, " {} waiting for verification🌀".format(ctx.message.author.mention))
    
  @commands.command(pass_context=True)
  async def verified(self, ctx, user: discord.User):
    if "528145435022327810" in(role.id for role in ctx.message.author.roles):
      await self.bot.send_message(user, "{} verification complete✅ \n"
                                  "You can now post **invite links** in **Join 4 Join** server \n"
                                  " \n"
                                  "You was verificate by {}".format(user.mention, ctx.message.author.mention))
      await self.bot.send_message(self.bot.get_channel('528209980734832642'), "{} was verificate✅".format(user.mention))
      return
    await self.bot.send_message(ctx.message.channel, "{} you don´t heve permissions to do that".format(ctx.message.author.mention))
    
  @commands.command(pass_context=True)
  async def verifyerror(self, ctx, user: discord.User):
    if "528145435022327810" in(role.id for role in ctx.message.author.roles):
      await self.bot.send_message(user, "❗verification error❗ \n"
                                  "{} you are not **Chicken Server** member \n"
                                  "If you want to get **verification** and enable post **invite links** \n"
                                  " \n"
                                  "Join **Chicken Server** \n"
                                  "https://discord.gg/9hjAVpP".format(user.mention))
      await self.bot.send_message(ctx.message.channel, "{} get verification error message".format(user.mention))
      return
    
def setup(bot):
  bot.add_cog(Verify(bot))