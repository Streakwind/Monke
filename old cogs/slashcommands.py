import discord
from discord.ext import commands
from discord import Member
import discord
from discord_slash import SlashCommand

class Slash (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash()
    async def test (ctx):
        await ctx.send("test")
    
    
def setup(bot):
    bot.add_cog(Slash(bot))
