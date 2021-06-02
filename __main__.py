import discord
from discord.ext import commands  
from discord import Member
import random
import traceback
import sys
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import config

description = ''' Hi, I'm a bot made by Streakwind#5347. Any questions? Down here is a list of commands. Realize that all commands in the Admin category can only be used by me.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=['a!', 'monke ', 'Monke ', 'A!'], owner_id=714554283026153554, description=description, intents=intents)

#async def status():
  #  async with aiohttp.ClientSession() as session:
  #      webhook = Webhook.from_url(config.webhook, adapter=AsyncWebhookAdapter(session))
  #      await webhook.send('Bot is ready!')
        
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print ('Monke for life!11!!!1!!')
    print('------')
    await bot.change_presence(activity=discord.Game('a!help'))
 #   await status()

@bot.event
async def on_disconnect():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(config.webhook, adapter=AsyncWebhookAdapter(session))
        await webhook.send('Disconnected from discord.', username='Status')
 
@bot.event
async def on_connect():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(config.webhook, adapter=AsyncWebhookAdapter(session))
        await webhook.send('Connected to discord!', username='Status')
 
@bot.listen('on_message')
async def direct_message(message):
        channel = bot.get_channel()
        if message.guild is None:
            if message.author.id != 736380975025619025:
                if message.author.id != 714554283026153554:
                   await channel.send(f"DIRECT MESSAGE\nTIME: {message.created_at}UTC\nFROM: {message.author} ({message.author.id})\nMESSAGE: {message.content}")

@bot.listen('on_command')
async def logging(ctx):
        channel = bot.get_channel()
        
        message = ctx.message
        
        destination = None
        if message.guild is None:
            destination = "Private Message"
        else:
            destination = f"#{message.channel} ({message.guild})"
            
        if message.author.id != 714554283026153554:
            await channel.send(f"{destination}\nTIME: {ctx.message.created_at}UTC\nFROM: {message.author} ({message.author.id})\nMESSAGE: {ctx.message.content}")

           
@bot.listen('on_message')
async def monke_bad_bot_lol(message):
        if message.content.startswith('monke bad bot'):
            await message.channel.send('I heard that <:wemeetagain:813559615639257129>')
            print (f"{message.author} said the bot is bad.")
        
initial_extensions = (
    'cogs.Hi',
    'cogs.Admin',
    'cogs.BasicCommands',
    'cogs.Main',
    'cogs.Moderation',
    'cogs.Music',
 #   'cogs.slashcommands',
    'cogs.eh',
)
"""
async def get_pre(bot, message):
  return "prefix"  # or a list, ["pre1","pre2"]

bot = commands.Bot(command_prefix=get_pre ...)
"""

bot.load_extension('jishaku')
for extension in initial_extensions:
  try:
     bot.load_extension(extension)
  except Exception as e:
     print(f'Failed to load extension {extension}.', file=sys.stderr)
     traceback.print_exc()
    
bot.run(config.token)
