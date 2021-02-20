import discord
from discord import commands

    @commands.command(
        name="play",
        aliases=["p", "yt"],
        usage="[song]",
    )
    # @commands.max_concurrency(1, commands.BucketType.guild, wait=True)
    async def play(self, ctx, *, search=None):
        """Play a song
        """
        if not ctx.player:
            player = self.create_player(ctx)
            ctx.player = player

        if (
            not search
            and ctx.player.is_playing
            and ctx.player.voice.is_paused()
            and ctx.author.guild_permissions.manage_guild
        ):
            ctx.player.resume()
            return await ctx.send(
                f"**:arrow_forward: Resuming** `{ctx.player.current.title}`"
            )

        if not search:
            return await ctx.send("Please specify a song to play/search for.")

        query, location_type = self.parse_search(search)

        await self.play_song(ctx, location_type, query)

         