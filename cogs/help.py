from discord.ext import commands

# Unimportant part
class MyHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        text = """ """
        embed = discord.embed(title = "Help", description=text, color=discord.Color.blue())
        channel = self.get_destination()
        await channel.send(embed=embed)
        
class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command))
        embed.add_field(name="Help", value=command.help)
        alias = command.aliases
        if alias:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

class YourCog(commands.Cog):
    def __init__(self, bot):
       self.bot = bot
        
       # Focus here
       # Setting the cog for the help
     #  help_command = MyHelp()
   #    help_command.cog = self # Instance of YourCog class
   #    help_command.command = MyHelpCommand()
     #  bot.help_command = help_command


def setup(bot):
    bot.add_cog(YourCog(bot))