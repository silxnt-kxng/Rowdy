from ast import alias

import disnake
from disnake import Message
from disnake.ext import commands
from disnake.ext.commands import has_guild_permissions
from disnake.ext.commands.cooldowns import BucketType
from disnake.ext.commands.core import cooldown

# from disnake.

smash_match = "TBD"
hearthstone_match = "TBD"
kart_match = "TBD"
nba_match = "TBD"
ovw_match = "TBD"

color = disnake.Color.from_rgb(12, 47, 107)

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="ping", alias=["pingpong"], description="Get the bot latency")
    @cooldown(1, 30, BucketType.user)
    async def pingpong(self, ctx):
        await ctx.send(f'Pong! 🏓 **{round(self.bot.latency * 1000)} ms**')
    
    @commands.slash_command(name="schedule", description="Get the weekly schedule")
    @cooldown(1, 60, BucketType.guild)
    async def schedule(self, ctx):
        await ctx.send(
            f'**This week\'s schedule**:\n Smash: {smash_match}\n Hearthstone: {hearthstone_match}\n Mario Kart: {kart_match}'
            )
    
    @commands.slash_command(name="poll", description="Run a poll")
    @cooldown(1, 30, BucketType.user)
    @has_guild_permissions(manage_messages=True)
    async def poll(self, ctx, *, question):
        pollEmbed = disnake.Embed(
            title=f"{ctx.author.name}'s poll!",
            description="\n",
            color=color
            )
        
        pollEmbed.add_field(
            name=f"{question}",
            value="Please react with one of the following: 👍, 👎, or 🤷"
        )
        await ctx.send(embed=pollEmbed)
    
    @commands.slash_command(name="servericon", description="Get the server icon (why do you need this???)")
    @cooldown(1, 30, BucketType.guild)
    @has_guild_permissions(administrator=True)
    async def servericon(self, ctx):
        url=ctx.guild.icon
        embed = disnake.Embed(
            title=f"{ctx.guild.name}'s Server Icon",
            color=color
        )
        embed.set_image(url=url)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))