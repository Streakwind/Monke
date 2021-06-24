import discord
from discord.ext import commands
from discord import Member
import random
import traceback
import sys

class Basic (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def calc(self, ctx, left, operator, right):
        """Calculates 2 numbers. (No fractions)"""
        if operator == '/':
            await ctx.send(left / right)
            
        if operator == '*':
            await ctx.send(left * right)
        
        if operator == '+':
            await ctx.send(left + right)
            
        if operator == '-':
            await ctx.send(left - right)
        
        else:
            await ctx.send("Invalid operation!")
            error = "".join(traceback.format_exception(type(e), e, e.__traceback__, 1))
            return await ctx.send(f"Error. Here's the traceback:\n```{error}```")
        
    
    @commands.command()
    async def info(self, ctx):
        """Information about the bot"""
        await ctx.send("Hi, I'm **Monke**. I was made by Streakwind. The bot started out using `https://github.com/Rapptz/discord.py/blob/master/examples/basic_bot.py` **__NOTE: This bot is still in development. Do not expect the most from it.__**")

    @commands.command()
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format. Example: a!roll 1d2"""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command()
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))

    @commands.command()
    async def joined(self, ctx, member: discord.Member = None):
        """Says when a member joined."""
        
        if not member:
            member = ctx.author
        await ctx.send('{0.name} joined in {0.joined_at} UTC'.format(member))
    
    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
       """Displays a specified users avatar"""
       if not member:
           member = ctx.author
       em = discord.Embed(title = str(member))
       em.set_image(url=member.avatar_url)
       await ctx.send(embed=em)
    
    @commands.command()
    async def prefix(self, ctx):
        """Prefixes for the bot"""
        await ctx.send("Current prefixes\n**1.** `Monke `\n**2.** `a!`\n**The prefixes are not case-sensitive**")

    
    @commands.command()
    async def ping(self, ctx):
        """The bots ping"""
        await ctx.send(f"My ping is {self.bot.latency * 1000}ms")
#@bot.group()
#async def cool(ctx):
#    """Says if a user is cool.
#   In reality this just checks if a subcommand is being invoked.
#   """
#    if ctx.invoked_subcommand is None:
#        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

#@cool.command(name='bot')
#async def _bot(ctx):
#    """Is the bot cool?"""
#    await ctx.send('Yes, the bot is cool.')

    @commands.command()
    async def say(self, ctx, *, msg):
        """Repeats what you say."""
        #print(f'{ctx.author} used a!say to say {msg}')
        await ctx.send(f"{msg}")

    @commands.command()
    async def rng(self, ctx, num1: int, num2: int):
        """Picks a random number between the two values"""
        value = random.randint(min(num1, num2), max(num1, num2))
        await ctx.send(f"You got {value}.")

def setup(bot):
    bot.add_cog(Basic(bot))