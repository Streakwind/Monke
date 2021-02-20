from discord.ext import commands
import discord

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def learn(self, ctx):
        """Tells you more about the bot"""
        await ctx.send (f"Hiya {ctx.author.mention}! Thanks for inviting **Monke**. Start out by using `a!info` or `a!help`! Have fun!")

    @commands.command(aliases = ["update"])
    async def updatelog(self, ctx):
        """Update log for the bot!"""
        await ctx.send ("**5 new features**\n\n`a!sourcecode`\n`Status changing commands (Admin only)`\n`a!learn`\n`a!messageowner`\n`Added the jishaku extension` ")
    @commands.command()
    async def messageowner(self, ctx, *, arg):
       """Sends the owner a message! """
       owner = self.bot.get_user(self.bot.owner_id)
       await owner.send(f"{ctx.author} has sent you a message!\n{arg}")
       await ctx.send(f"Succesfully sent {arg}")
    @commands.command()
    async def sourcecode(self, ctx):
        """Don't....."""
        await ctx.send("<https://github.com/Streakwind/Monke>")

    @commands.command()
    async def secret(self, ctx):
        """I wonder what this does...."""
        await ctx.send("```Never gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you```")
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, banreason=None):
      """Bans a specified user from the guild"""
      await member.ban(reason=banreason)
      await ctx.send(f"{member} has been banned by {ctx.author}. Reason: {banreason}")
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, kickreason=None):
      """Kicks a specified user from the guild"""
      await member.kick(reason=kickreason)
      await ctx.send(f"{member} has been kicked by {ctx.author}. Reason: {kickreason}")
               
def setup(bot):
    bot.add_cog(Main(bot))
