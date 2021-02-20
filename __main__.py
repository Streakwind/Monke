# This example requires the 'members' privileged intents

import discord
from discord.ext import commands
from discord import Member
import random
import traceback
import sys

description = ''' Hi, I'm a bot made by Streakwind#5347. Any questions? Down here is a list of commands'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='a!', owner_id=714554283026153554, description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print ('The bot is on!')
    print('------')
    await bot.change_presence(activity=discord.Game('a!help'))
    
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
    
bot.run("NzM2MzgwOTc1MDI1NjE5MDI1.Xxt-OQ.ceawzDVTW15hJgEtNoNs2Nc2PuA")