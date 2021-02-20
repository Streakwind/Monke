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
    async def add(self, ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)
    
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
    async def repeat(self, ctx, times: int, content='repeating...'):
        """Repeats a message, use quotes.(Discord ratelimit: 5mps)"""
        for i in range(times):
            await ctx.send(content)

    @commands.command()
    async def joined(self, ctx, member: discord.Member):
        """Says when a member joined."""
        await ctx.send('{0.name} joined in {0.joined_at}    UTC'.format(member))
    
    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
       """Displays a specified users avatar"""
       if not member:
           member = ctx.author
       em = discord.Embed()
       em.set_image(url=member.avatar_url)
       await ctx.send(embed=em)

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
    async def say(self, ctx, msg):
        """Repeats what you say. Use quotes."""
        await ctx.send(f"{msg}")

    @commands.command()
    async def rng(self, ctx, num1: int, num2: int):
        """Picks a random number between the two values"""
        value = random.randint(min(num1, num2), max(num1, num2))
        await ctx.send(f"You got {value}.")

def setup(bot):
    bot.add_cog(Basic(bot))