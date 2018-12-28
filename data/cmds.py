import discord
from discord.ext import commands

class Cmds:
  def __init__(self, bot):
    self.bot = bot
    
  async def on_message(self, message):
    if message.content.startswith('test'):
      await self.bot.send_message(message.channel, 'test')
      
  @commands.command(pass_context=True)
  async def clear(self, ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in self.bot.logs_from(channel, limit=int(amount) + 1):
      messages.append(message)
    await self.bot.delete_messages(messages)
    await self.bot.say("messages deleted")
    
  @commands.command(pass_context=True)
  async def dm(self, ctx):
    await self.bot.send_message(ctx.message.channel," test dm \n"
                                "by user {} ".format(ctx.message.author.mention)
    await self.bot.send_message(server_member, "test")

    
    
def setup(bot):
  bot.add_cog(Cmds(bot))
