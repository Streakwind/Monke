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
        await ctx.send ("**5 new features**\n\n`a!sourcecode`\n`Status changing commands (Admin only)`\n`a!secret`\n`a!messageowner`\n`a!kick and a!ban` ")
    @commands.command()
    async def messageowner(self, ctx, *, arg):
       """Sends the owner a message! """
       owner = self.bot.get_user(self.bot.owner_id)
       await owner.send(f"{ctx.author} has sent you a message!\n{arg}")
       await ctx.send(f"Succesfully sent {arg}")
    @commands.command()
    async def sourcecode(self, ctx):
        """Don't....."""
  #      print (f'{ctx.author} used a!sourcecode')
        message = ctx.message
    
        destination = None
        if ctx.guild is None:
            destination = "Private Message"
            guild_id = None
        else:
            destination = f"#{message.channel} ({message.guild})"
            guild_id = ctx.guild.id
        
        print(f"TIME:{message.created_at}\n{ctx.author} used source code at {destination}\n")
        await ctx.send("<https://github.com/Streakwind/Monke>")

    @commands.command(hidden=True)
    async def secret(self, ctx):
        """I wonder what this does...."""
        secret = """
        Never gonna give you up
        Never gonna let you down
        Never gonna run around and desert you
        Never gonna make you cry
        Never gonna say goodbye
        Never gonna tell a lie and hurt you
        """
        em = discord.Embed(description=secret, color=discord.Color.blue())
        await ctx.send(embed = em)
    
    @commands.command()
    async def invite(self, ctx):
        """Gives you the invite link for the bot."""
        await ctx.send(f"Here is the invite link {ctx.author.mention} <https://discord.com/api/oauth2/authorize?client_id=736380975025619025&permissions=271969350&scope=bot>")

               
def setup(bot):
    bot.add_cog(Main(bot))

