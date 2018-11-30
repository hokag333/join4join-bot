import discord
from discord.ext import commands

class Reply:
  def __init__(self, bot):
    self.bot = bot
    
  
  async def on_message(self, message):
    if message.content.startswith('egg'):
      await self.bot.send_message(message.channel, ':egg:')
      
    if message.content.startswith('chicken'):
      await self.bot.send_message(message.channel, ':hatched_chick:')
      
    if ('shit') in message.content:
      await self.bot.send_message(message.channel, ':poop:')
      
    if message.content.startswith('how are you'):
      await self.bot.send_message(message.channel, ' ** :hatched_chick: I am fine tnx :hatched_chick: ** ')
      
    if message.content.startswith('How are you'):
      await self.bot.send_message(message.channel, ' ** :hatched_chick: I am fine tnx :hatched_chick: ** ')
      
    if message.content.startswith('Hi'):
      await self.bot.send_message(message.channel, ':hatched_chick: **Hello** :hatched_chick: ')
      
    if message.content.startswith('hi'):
      await self.bot.send_message(message.channel, ':hatched_chick: **Hello** :hatched_chick: ')
      
    if message.content.startswith('whats up'):
      await self.bot.send_message(message.channel, ' **I am good u** ')
      
    if message.content.startswith('damn'):
      await self.bot.send_message(message.channel, '**fool**')
      
    if message.content.startswith('owner'):
      await self.bot.send_message(message.channel, 'The server owner is <@381887710308335618>')
      
    if message.content.startswith('website'):
      await self.bot.send_message(message.channel, '**server website :** https://chickenserver.wix.com/website')
      
    if ('duck') in message.content:
      await self.bot.send_message(message.channel, 'quack')
      
    if message.content.startswith('knock knock'):
      await self.bot.send_message(message.channel, 'who is there?!')
      
    if message.content.startswith('Hey!'):
      await self.bot.send_message(message.channel, 'Yeah boy')
      
    if message.content.startswith('train'):
      await self.bot.send_message(message.channel, ':bullettrain_front:')
      
    if ('good night') in message.content:
      await self.bot.send_message(message.channel, '<:sleepingegg:508556018779947030>')
      
    if message.content.startswith('ho is playing in the beginning'):
      await self.bot.send_message(message.channel, 'EMINƎM')
      
    if ('mother fucker') in message.content:
      await self.bot.send_message(message.channel, 'machine gun kelly')
      
    if message.content.startswith('fast'):
      await self.bot.send_message(message.channel, 'Uh‚ sama lamaa duma lamaa you \n'
                                 'assuming I am a human \n'
                                 'What I gotta do to get it through \n'
                                 'to you I am superhuman \n'
                                 'Innovative and I am made of rubber \n'
                                 'So that anything you saying ricocheting \n'
                                 'off of me and it will glue to you \n'
                                 'I am never stating‚ more than \n'
                                 'never demonstrating \n'
                                 'How to give a motherfuckin audience \n'
                                 'a feeling like It is levitating \n'
                                 'Never fading‚ and I know that the \n'
                                 'haters are forever waiting \n'
                                 'For the day that they can say I fell \n'
                                 'off‚ They had be celebrating \n'
                                 'Cause I know the way to \n'
                                 'get them motivated \n'
                                 'I make elevating music‚ you \n'
                                 'make elevator music \n')
      
  @commands.command()
  async def ping(self):
    await self.bot.say('bang')
    
def setup(bot):
  bot.add_cog(Reply(bot))
