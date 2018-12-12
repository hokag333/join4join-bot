import discord
from discord.ext import commands

class Points:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.author.bot: return
    
    if message.content.startswith('!points help'):
      await self.bot.send_message(message.channel, " **{}** \n"
                                  "**!points** to show your/user´s points \n"
                                  "**!points register** if you are not registered".format(message.author.name))
      
    if message.content.startswith('!points register'):
      await self.bot.send_message(self.bot.get_channel('520911898909212676'), ' **{}**  was registered to points member list'.format(message.author.name))
  
  @commands.command(pass_context=True)
  async def coinflip(self, ctx, guess: str, amount: float):
    guesses = ('heads', 'tails')
    guess = guess.lower()
    if guess not in guesses:
      await self.bot.say("Invalid guess.")
      return
    author = ctx.message.author
    balance = get_dollars(author)
    if balance < amount:
      await self.bot.say(f"You don't have that much money.  Your balance is ${balance:.2f}")
      return
    result = random.sample(guesses)
    if result == guess:
      await self.bot.say("You won!")
      add_dollars(author, amount)
    else:
      await self.bot.say("You lost!")
      remove_dollars(author, amount)
      
  @commands.command(pass_context=True)
  async def points(self, ctx, user: discord.User=None):
    if not user:
      #4835
      if "381887710308335618" in (ctx.message.author.id):
        await self.bot.say(" **{}** you have **∞** points".format(ctx.message.author.name))
        return
      #7553
      if "461967586058305537" in (ctx.message.author.id):
        await self.bot.say(" **{}** you have **5 500** points".format(ctx.message.author.name))
        return
      #1056
      if "466673021248208896" in (ctx.message.author.id):
        await self.bot.say(" **{}** you have **1 000** points".format(ctx.message.author.name))
        return
      #3046
      if "310264325497421824" in (ctx.message.author.id):
        await self.bot.say(" **{}** you have **1 000** points".format(ctx.message.author.name))
        return
      #6739
      if "373867168280084496" in (ctx.message.author.id):
        await self.bot.say(" **{}** you have **500** points".format(ctx.message.author.name))
        return
      else:
        await self.bot.say(" **{}** you haven't got any points \n"
                           "or not registered **(!points help)**".format(ctx.message.author.name))
    #user.list
    else:
      #4835
      if "381887710308335618" in (user.id):
        await self.bot.say(" **{}** have **∞** points".format(user.name))
        return
      #7553
      if "461967586058305537" in (user.id):
        await self.bot.say(" **{}** have **5 500** points".format(user.name))
        return
      #1056
      if "466673021248208896" in (user.id):
        await self.bot.say(" **{}** have **1 000** points".format(user.name))
        return
      #3046
      if "310264325497421824" in (user.id):
        await self.bot.say(" **{}** have **1 000** points".format(user.name))
        return
      #6739
      if "373867168280084496" in (user.id):
        await self.bot.say(" **{}** have **500** points".format(user.name))
        return
      else:
        await self.bot.say(" **{}** haven't got any points".format(user.name))
        
        
def setup(bot):
  bot.add_cog(Points(bot))
