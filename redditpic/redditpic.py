from typing import Literal
import aiohttp
import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]


class RedditPic(commands.Cog):
    """
    Get a random picture from Reddit subreddits.
    """

    # Version
    __version__ = "1.0.3"

    # Cookiecutter things
    def __init__(self, bot: Red) -> None:
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=572944636209922059,
            force_registration=True,
        )

    async def red_delete_data_for_user(
        self, *, requester: RequestType, user_id: int
    ) -> None:
        # TODO: Replace this with the proper end user data removal handling.
        super().red_delete_data_for_user(requester=requester, user_id=user_id)

    # Comamnd code

    @commands.command()
    async def randmeme(self, ctx):
        """Get a random meme from r/memes"""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://imageapi.fionn.live/reddit/memes"
            ) as request:
                response = await request.json()
                embed = discord.Embed(color=(await ctx.embed_colour()))
                embed.set_image(url=response["img"])
                embed.add_field(
                    name=response["title"],
                    value=f"Posted by u/{response['author']}\nCan't see the picture? [Click here]({response['img']})",
                )
                embed.set_footer(
                    text=f"{response['upvotes']} 👍 {response['downvotes']} 👎 | Posted on: r/{response['endpoint']} | Took {response['took']}"
                )
                await ctx.send(embed=embed)

    @commands.command()
    async def subr(self, ctx, subreddit):
        """Get a random picture from a subreddit \n\n If an error occurs, please wait a few seconds, then try again."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                f"https://imageapi.fionn.live/reddit/{subreddit}"
                ) as request:
                    response = await request.json()
        except {response['err']}:
            await ctx.send("test")

                embed = discord.Embed(color=(await ctx.embed_colour()))

                embed.set_image(url=response["img"])
                embed.add_field(
                    name=response["title"],
                    value=f"Posted by u/{response['author']}\nCan't see the picture? [Click here]({response['img']})",
                )
                embed.set_footer(
                    text=f"{response['upvotes']} 👍 {response['downvotes']} 👎 | Posted on: r/{response['endpoint']} | Took {response['took']}"
                )
                await ctx.send(embed=embed)

    @commands.command()
    async def memeversion(self, ctx):
        """Find cog version"""
        await ctx.send(f"This cog is on version 1.0.3")
