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
        await ctx.send ("**5 new features**\n\n`Added a messaging system`\n`Upgraded messageowner command`\n`Bug fixes on some commands`\n`Finally got reactions to work (Admin-only command)`\n`Logging!`")
    @commands.command()
    async def messageowner(self, ctx, *, arg:str):
       """Sends the owner a message! """
       owner = self.bot.get_user(self.bot.owner_id)
   #    await owner.send(f"{ctx.message.channel} ({ctx.message.guild})\n{ctx.author} ({ctx.author.id}) has sent you a message!\n{arg}")
       await owner.send(f"{ctx.author} ({ctx.author.id}): {arg}")
       await ctx.send(f"Succesfully sent {arg}")
    @commands.command()
    async def sourcecode(self, ctx):
        """Don't....."""
  #      print (f'{ctx.author} used a!sourcecode')
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
    @commands.command()
    async def message(self, ctx, userid:int, *, message):
        """Message another person (Use a!userid person to find their userid)"""
        person = self.bot.get_user(userid)
        await person.send(f"{ctx.author}: {message}\nBy the way, use `a!message yourmessagehere {ctx.author.id}` to message them back")
        await ctx.send(f"Succesfully sent {message}")
    
    @commands.command()
    async def userid(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        await ctx.send(f"{member}'s user id is {member.id}")
        
    @commands.command(aliases = ["ui"])
    async def userinfo(self, ctx, member: discord.Member = None):
        isbot = ":x:"
        
        if not member:
            member = ctx.author
            
        embed = discord.Embed(description=member, color=discord.Color.blue())
      #  embed.set_thumbnail(*, member.avatar_url)
            
       # if member.bot == true:
          #  isbot = "YES"
 #       await ctx.send(f"{member}\nUSERID:{member.id}\nBOT:{isbot}\nAVATAR:{member.avatar_url}")
        await ctx.send(embed = embed)
               
def setup(bot):
    bot.add_cog(Main(bot))
