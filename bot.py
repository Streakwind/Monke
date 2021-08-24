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
import datetime

description = ''''''

def get_prefix(bot, message):
  return ["a!", "monke "]

intents = discord.Intents.default()
intents.members = True
            
initial_extensions = (
    'cogs.admin',
    'cogs.moderation',
    'cogs.music',
    'cogs.fun',
    'cogs.information',
    'cogs.stats',
)
    
class Monke(commands.Bot):
    def __init__(self):
        self.uptime=datetime.datetime.utcnow()
        
        super().__init__(
            command_prefix=get_prefix,
            description=description,
            owner_id=714554283026153554,
            intents=intents,
        )
        
        self.load_extension('jishaku')
    
        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()
         
        
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('TIME: %(asctime)s, LEVEL: %(levelname)s, NAME: %(name)s: %(message)s'))
    logger.addHandler(handler)
    
    #async def bot_setup(self):
        #self.uptime=datetime.datetime.utcnow()        
        
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print ('Monke for life!11!!!1!!')
        print('------')
        await self.change_presence(activity=discord.Game('a!help'))
        
 
    async def on_disconnect(self):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(config.webhook, adapter=AsyncWebhookAdapter(session))
            await webhook.send('Disconnected from discord.', username='Status')

    async def on_connect(self):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(config.webhook, adapter=AsyncWebhookAdapter(session))
            await webhook.send('Connected to discord!', username='Status')
            
    async def on_resumed(self):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(config.webhook, adapter=AsyncWebhookAdapter(session))
            await webhook.send('Resumed connection to discord!', username='Status')
        
    @commands.Cog.listener('on_message')
    async def direct_message(self, message):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(config.logging_webhook, adapter=AsyncWebhookAdapter(session))  
            if message.guild is None:
                if message.author.id != 736380975025619025:
                    if message.author.id != 714554283026153554:
                        embed = discord.Embed(title="DIRECT MESSAGE")
                        embed.add_field(name="TIME", value=f"{message.created_at}UTC")
                        embed.add_field(name="FROM", value=f"{message.author} ({message.author.id})")
                        embed.add_field(name="MESSAGE", value=f"{message.content}")
                        embed.set_thumbnail(url=message.author.avatar_url) 
                        #await webhook.send(f"```DIRECT MESSAGE\nTIME: {message.created_at}UTC\nFROM: {message.author} ({message.author.id})\nMESSAGE: {message.content}```", username='Direct Message Log')
                        await webhook.send(embed = embed, username = "Direct Message Log")
                    
    @commands.Cog.listener('on_command')
    async def logging(self, message):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(config.logging_webhook, adapter=AsyncWebhookAdapter(session))
       #     channel = bot.get_channel(849678967639638057)
   
            #channel.send("something")
            destination = None     
            if message.guild != None:
                if message.author.id != 714554283026153554:
                    destination = f"#{message.channel} ({message.guild})"
                
                    embed = discord.Embed(title=f"{destination}")
                    embed.add_field(name="TIME", value=f"{message.created_at}UTC")
                    embed.add_field(name="FROM", value=f"{message.author} ({message.author.id})")
                    embed.add_field(name="MESSAGE", value=f"{message.content}")
                    embed.set_thumbnail(url=message.author.avatar_url)
                    #await webhook.send(f"```{destination}\nTIME: {ctx.message.created_at}UTC\nFROM: {message.author} ({message.author.id})\nMESSAGE: {ctx.message.content}```", username= 'Log')
                    await webhook.send(embed=embed, username="Log")
               
    @commands.Cog.listener('on_message')
    async def monke_bad_bot_lol(self, message):
        if message.content.startswith('monke bad bot'):
            await message.channel.send('I heard that <:wemeetagain:813559615639257129>')
            print (f"{message.author} said the bot is bad.")

    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(config.guild_webhook, adapter=AsyncWebhookAdapter(session))
    
            if message_after.guild.id == 812439278000406590:
            
                embed = discord.Embed(title=f"{message_after.author} has edited a message!")
                embed.add_field(name="TIME", value=f"{message_after.created_at}UTC")
                embed.add_field(name="LINK", value=f"{message_after.jump_url}")
                embed.add_field(name="BEFORE", value=f"{message_before.content}", inline=True)
                embed.add_field(name="AFTER", value=f"{message_after.content}", inline=True)
                embed.set_thumbnail(url=message_after.author.avatar_url)
                
                #await webhook.send(f"{message_after.author} has edited a message.\n{message_after.jump_url}\nPrevious: {message_before.content}\nNew: {message_after.content}", username = 'Guild Log')
                await webhook.send(embed=embed, username="Guild Log")
            
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(config.guild_webhook, adapter=AsyncWebhookAdapter(session))
    
            if message.guild.id == 812439278000406590:
                embed = discord.Embed(title=f"{message.author} has deleted a message!")
                embed.add_field(name="TIME", value=f"{message.created_at}UTC")
                embed.add_field(name="MESSAGE", value=f"{message.content}")
                embed.set_thumbnail(url=message.author.avatar_url)           
               # await webhook.send(f"{message.author} has deleted a message.\nMessage: {message.content}", username = 'Guild Log')
                await webhook.send(embed=embed, username="Guild Log")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(config.logging_webhook, adapter=AsyncWebhookAdapter(session))
        
            """The event triggered when an error is raised while invoking a command.
            Parameters
            ------------
            ctx: commands.Context
                The context used for command invocation.
            error: commands.CommandError
                The Exception raised.
            """
            if hasattr(ctx.command, 'on_error'):
                return

            cog = ctx.cog
            if cog:
                if cog._get_overridden_method(cog.cog_command_error) is not None:
                    return

            #ignored = (commands.CommandNotFound, )
            error = getattr(error, 'original', error)

            #if isinstance(error, ignored):
                #return
            
    #        if isinstance(error, commands.CommandNotFound):
   #             await ctx.send(":x: Command not found")
                
  #          if isinstance(error, commands.DisabledCommand):
 #               await ctx.send(f'{ctx.command} has been disabled.')

#            elif isinstance(error, commands.NoPrivateMessage):
         #       try:
        #            await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
       #         except discord.HTTPException:
      #              pass

     #       elif isinstance(error, commands.BadArgument):
    #            if ctx.command.qualified_name == 'tag list':
   #                 await ctx.send('I could not find that member. Please try again.')
            
            embed_1 = discord.Embed(title="Command Error", description=f"Ignoring exception in command {ctx.command}", color=discord.Color.blue())
            embed_1.add_field(name="Error", value=f"`{str(error)}`")
            
            await ctx.send(embed=embed_1)
            
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
    
            embed = discord.Embed(title=f"Command Error - Time: {ctx.message.created_at}", description=f"Ignoring exception in command {ctx.command}", color=discord.Color.blue())
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.add_field(name="Error", value=f"`{str(error)}`")
            embed.add_field(name="Command User", value=f"{ctx.author} - {ctx.author.id}")
            
            await webhook.send(embed=embed)
            
    @commands.Cog.listener('on_raw_reaction_add')
    async def on_raw_reaction_add(self, reaction):
        print ("Hello")
        
        guild = self.get_guild(reaction.guild_id)
        
        if str(reaction.emoji) == '\U00002705':
            print("1")
            
            if str(reaction.message_id) == '874421110115041311':  
                print("2")
                
                role = guild.get_role('874421249550454837')
                
                await reaction.member.add_roles(role)

bot = Monke()

bot.help_command = commands.MinimalHelpCommand()

@bot.command(hidden=True)
async def hello(ctx):
    await ctx.send (f"Hello, {ctx.author.mention}. You can use `a!help` to get started.")
    
bot.run(config.token)