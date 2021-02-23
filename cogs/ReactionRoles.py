import discord
from discord.ext import commands

class ReactionRoles (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=["reactionroles"])
    async def setuprr(self, ctx, messageid, roleid):
        self.role_message_id = messageid
        
def setup(bot):
    bot.add_cog(ReactionRoles(bot))
