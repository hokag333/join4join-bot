import discord
from discord.ext import commands

class Commands:
  def __init__(self, bot):
    self.bot = bot
    
  async def on_message(self, message):
    if ('discord.gg') in message.content:
      if "528162784022626314" in(role.id for role in message.author.roles):
        return
      else:
        await self.bot.delete_message(message)
    
  async def on_command_error(self, error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
      await self.bot.send_message(ctx.message.channel, content="You have %.6s s cooldown on this command" % error.retry_after)
      await asyncio.sleep(20)
      await self.bot.delete_message(message)
      raise error
      
  @commands.command(pass_context=True)
  @commands.cooldown(1, 60*60*24, commands.BucketType.user)
  async def dm(self, ctx, *, reason=""):
    if "528160233273425923" in(role.id for role in ctx.message.author.roles):
      await self.bot.delete_message(ctx.message)
      await self.bot.send_message(ctx.message.channel, "{}\n"
                                  " \n"
                                  "**Join 4 Join dm** by {} \n"
                                  "don´t forget to contact him to make join 4 join".format(reason, ctx.message.author.mention))
    else:
      await self.bot.send_message(ctx.message.channel, "{} you don´t have permissions to dm command".format(ctx.message.author.mention))
    
  @commands.command(pass_context=True)
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
    await self.bot.send_message(self.bot.get_channel('528209980734832642'), " {} waiting for verification🌀".format(ctx.message.author.mention))
    
  @commands.command(pass_context=True)
  async def verified(self, ctx, user: discord.User):
    if "528145435022327810" in(role.id for role in ctx.message.author.roles):
      await self.bot.send_message(user, "{} verification complete✅ \n"
                                  "You can now post **invite links** in **Join 4 Join** server \n"
                                  " \n"
                                  "You was verificate by {}".format(user.mention, ctx.message.author.mention))
      await self.bot.send_message(ctx.message.channel, "{} was verificate".format(user.mention))
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
  bot.add_cog(Commands(bot))
