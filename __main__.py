import discord
from discord.ext import commands
from discord import Member
import random
import traceback
import sys

description = ''' Hi, I'm a bot made by Streakwind#5347. Any questions? Down here is a list of commands. Realize that all commands in the Admin category can only be used by me.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='a!', owner_id=714554283026153554, description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print ('Monke for life!11!!!1!!')
    print('------')
    await bot.change_presence(activity=discord.Game('a!help'))

@bot.listen('on_message')
async def monke_bad_bot_lol(message):
        if message.content.startswith('monke bad bot'):
            await message.channel.send('I heard that <:wemeetagain:803413513212133406>')
            print (f"{message.author} said the bot is bad.")
        
initial_extensions = (
    'cogs.Hi',
    'cogs.Admin',
    'cogs.BasicCommands',
    'cogs.Main',
)

bot.load_extension('jishaku')
for extension in initial_extensions:
  try:
     bot.load_extension(extension)
  except Exception as e:
     print(f'Failed to load extension {extension}.', file=sys.stderr)
     traceback.print_exc()
    
bot.run("n o")
