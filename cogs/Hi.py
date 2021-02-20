from discord.ext import commands
import discord

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome to the server {0.mention}! I hope you enjoy your time here.'.format(member))
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('{0.name} has left the server.'.format(member))

    @commands.command(aliases=["hi"])
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}!'.format(member))
        else:
            await ctx.send('Hello {0.name}!'.format(member))
        self._last_member = member
#    @commands.command()  # this is automatically registered to MyCog
#    async def hi(self, ctx):
#        """Say hi!"""
#        await ctx.send(f"hiii {ctx.author.mention}!!!")
    
def setup(bot):
    bot.add_cog(Greetings(bot))