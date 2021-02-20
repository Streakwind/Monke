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
        await ctx.send ("**5 new features**\n\n`a!reload (admin-only command)`\n`a!updatelog`\n`a!learn`\n`Added aliases to updatelog and hello`\n`Moved some commands` ")
    @commands.command()
    async def messageowner(self, ctx, *, arg):
       """Sends the owner a message! """
       owner = self.bot.get_user(self.bot.owner_id)
       await owner.send(f"{ctx.author} has sent you a message!\n{arg}")
       await ctx.send(f"Succesfully sent {arg}")
# Setting `Playing ` status
#await bot.change_presence(activity=discord.Game(name="a game"))

# Setting `Streaming ` status
#await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Setting `Listening ` status
#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

#this is how "Competing in" is set.
#discord.Activity(name="Test", type=5)

def setup(bot):
    bot.add_cog(Main(bot))
