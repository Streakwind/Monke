from discord.ext import commands
import discord
from discord import Member
import random
import traceback
import sys

class Information(commands.Cog):
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
    
    @commands.command()
    async def info(self, ctx):
        """Information about the bot"""
        await ctx.send("Hi, I'm **Monke**. I was made by Streakwind. The bot started out using <https://github.com/Rapptz/discord.py/blob/master/examples/basic_bot.py> **__NOTE: This bot is still in development. Do not expect the most from it.__**")
    @commands.command()
    async def sourcecode(self, ctx):
        """Don't....."""
        await ctx.send("<https://github.com/Streakwind/Monke>")
    
    @commands.command()
    async def userid(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        await ctx.send(f"{member}'s user id is {member.id}")
        
    @commands.command(aliases = ["ui"])
    async def userinfo(self, ctx, *, member: discord.Member = None):
        isbot = ":x:"
        
        if not member:
            member = ctx.author
        
        time = str(ctx.message.created_at)[:19]
        embed = discord.Embed(title="ALL TIMES ARE IN UTC", description="", color=discord.Color.blue())
        embed.set_author(name=f"{member}, {member.id}", icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(icon_url="https://images-ext-2.discordapp.net/external/dAn5X2wnC6ZXQ1R2Gc-KR4cTBiKv7gTxQlWQZXIq0xc/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/736380975025619025/ab9e6644e42342400080d8dc3ce6afd3.webp?width=80&height=80", text=f"Monke | {time} ")
        embed.add_field(name="User created at", value=str(member.created_at)[:19], inline=True)
        
        if ctx.guild: 
            if member in ctx.guild.members:
                embed.add_field(name="User joined at", value=str(member.joined_at)[:19], inline=True)
            else:
                embed.description += f"This user ({member}) is not in the guild"
        
        if member.bot:
            embed.description += "This user is a bot"
            
        if ctx.guild:     
            if member.id == ctx.guild.owner.id:
                embed.description += f"\nThis user owns this server ({ctx.guild.name})"
     #   embed.author.icon_url(url=member.avatar_url)
            
       # if member.bot == true:
          #  isbot = "YES"
 #       await ctx.send(f"{member}\nUSERID:{member.id}\nBOT:{isbot}\nAVATAR:{member.avatar_url}")
        await ctx.send(embed = embed)
    
    @commands.command(aliases = ["gi"])
    async def guildinfo(self, ctx):   
        
        guild = ctx.guild
        
        if ctx.guild:
            embed = discord.Embed(title="TIMES ARE CONVERTED INTO YOUR TIME ZONE", description="", color=discord.Color.blue())
            embed.set_author(name=f"{guild} - {guild.id}", icon_url=guild.icon_url)
            embed.set_thumbnail(url=guild.icon_url)
            embed.add_field(name="Guild Owner", value=guild.owner, inline=True)
            embed.set_footer(icon_url="https://images-ext-2.discordapp.net/external/dAn5X2wnC6ZXQ1R2Gc-KR4cTBiKv7gTxQlWQZXIq0xc/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/736380975025619025/ab9e6644e42342400080d8dc3ce6afd3.webp?width=80&height=80", text=f"Monke")
            embed.add_field(name="Guild created at", value=str(guild.created_at)[:19], inline=True)
            embed.add_field(name="Members", value=guild.member_count, inline=True)
            embed.add_field(name="Emojis", value=guild.emojis, inline=True)
            embed.add_field(name="Emoji limit", value=guild.emoji_limit, inline=True)
            embed.add_field(name="Text channels", value=guild.text_channels, inline=True)
            embed.add_field(name="Voice channels", value=guild.voice_channels, inline=True)
      #      embed.timestamp(str(ctx.message.created_at)[:19])
            await ctx.send(embed = embed)
        
        else:
            await ctx.send("This command can only be used in guilds/servers!")
#    @commands.command()
 #   async def uptime(self, ctx):
  #      uptime = self.bot.uptime
   #     await ctx.send(f"{uptime}")
        
               
def setup(bot):
    bot.add_cog(Information(bot))
