import discord
from discord.ext import commands  
from discord import Member
import random
import traceback
import sys
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import config
import logging

description = ''''''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=['a!', 'monke ', 'Monke ', 'A!', '<@!736380975025619025>'], owner_id=714554283026153554, description=description, intents=intents)
bot.help_command = commands.MinimalHelpCommand()
bot.help_command.hidden=True
#async def status():
  #  async with aiohttp.ClientSession() as session:
  #      webhook = Webhook.from_url(config.webhook, adapter=AsyncWebhookAdapter(session))
  #      await webhook.send('Bot is ready!')
  
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('TIME: %(asctime)s, LEVEL: %(levelname)s, NAME: %(name)s: %(message)s'))
logger.addHandler(handler)

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


        
@bot.event        
async def on_resumed():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(config.webhook, adapter=AsyncWebhookAdapter(session))
        await webhook.send('Resumed connection to discord!', username='Status')
        
@bot.listen('on_message')
async def direct_message(message):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(config.logging_webhook2, adapter=AsyncWebhookAdapter(session))  
        if message.guild is None:
           if message.author.id != 736380975025619025:
                if message.author.id != 714554283026153554:
                    await webhook.send(f"```DIRECT MESSAGE\nTIME: {message.created_at}UTC\nFROM: {message.author} ({message.author.id})\nMESSAGE: {message.content}```", username='Owner Direct Message Log')
            
@bot.listen('on_command')
async def logging(ctx):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(config.logging_webhook, adapter=AsyncWebhookAdapter(session))
   #     channel = bot.get_channel(849678967639638057)
        
        message = ctx.message
        
        #channel.send("something")
        destination = None     
        if message.guild != None:
            if message.author.id != 714554283026153554:
                destination = f"#{message.channel} ({message.guild})"
                await webhook.send(f"```{destination}\nTIME: {ctx.message.created_at}UTC\nFROM: {message.author} ({message.author.id})\nMESSAGE: {ctx.message.content}```", username= 'Log')
           
@bot.listen('on_message')
async def monke_bad_bot_lol(message):
        if message.content.startswith('monke bad bot'):
            await message.channel.send('I heard that <:wemeetagain:813559615639257129>')
            print (f"{message.author} said the bot is bad.")

@bot.listen('on_message_edit')
async def message_edit(message):
    webhook = Webhook.from_url(config.guild_webhook, adapter=AsyncWebhookAdapter(session))

    if message.guild.id == 812439278000406590:
        await webhook.send(f"{message.author} has edited a message ({message.id}).\nPrevious: {message.before})\nNew: {message.after}", username = 'Guild Log Test')
        
@bot.command(hidden=True)
async def hello(ctx):
    await ctx.send (f"Hello, {ctx.author.mention}. You can use `a!help` to get started.")
    
initial_extensions = (
  #  'cogs.Hi',
    'cogs.Admin',
 #   'cogs.BasicCommands',
 #   'cogs.Main',
    'cogs.Moderation',
    'cogs.Music',
 #   'cogs.slashcommands',
 #   'cogs.eh',
 #   'cogs.help',
    'cogs.fun',
    'cogs.information',
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