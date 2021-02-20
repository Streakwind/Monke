from discord.ext import commands
import discord

#class HelpCommand(commands.HelpCommand):
    #async def send_bot_help(self, mapping):
        # here is where you send the main help command message.
        # you can get all the commands with `bot.commands()`.
        # self.bot exists here, and self.context too if you need it (which is ctx)

    #async def send_cog_help(self, cog):
        # this is where you send the cog help command message.
        # you can get all of a cog's commands with `cog.commands`

    #async def send_group_help(self, group):
        # this is where you send the group help command message.
        # you can get all of a group's subcommands with `group.commands`

    #async def send_command_help(self, group):
        # this is where you send the command help command message.
        # this is similar to send_group_help, but you don't need to worry about subcommands
        
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
    @commands.command()
    async def sourcecode(self, ctx)
        """Don't....."""
        await ctx.send(f"`https://github.com/Streakwind/Monke`")
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
