from platform import python_version

import disnake
from disnake import __version__ as disnake_version
from disnake.ext import commands
from disnake.ext.commands import has_guild_permissions
from disnake.ext.commands.cooldowns import BucketType
from disnake.ext.commands.core import cooldown
import DiscordUtils

owner = [422835542653272066, 951235151860486175]

description = "< > is required | [ ] is optional"
big = 'https://images-ext-1.discordapp.net/external/7B7-B9v60cV7uSaVhI8tPPNSnqzlTn0_5O-vOAFdf0Y/%3Fsize%3D1024/https/cdn.discordapp.com/icons/614172008044822569/339afe000ee54a1b08c8ac384247e487.png'
color = disnake.Color.from_rgb(12, 47, 107)
footer = "Alex and Dr. Perry can ban people from this bot at their discretion"

class HelpMenu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="modhelp", description="Help for the mods")
    @cooldown(1, 30, BucketType.user)
    @has_guild_permissions(administrator=True)
    async def modhelp(self, ctx):
        modem = disnake.Embed(
            title="Moderation Help",
            color=color
        )
        modem.add_field(
            name="giverole <@user>",
            value="Give roles"
        )
        modem.add_field(
            name="removerole <@user>",
            value="Remove roles"
        )
        modem.add_field(
            name="servericon",
            value="This was more for me (Alex) but go nuts"
        )
        modem.add_field(
            name="mute <@user>",
            value="Gives someone the Shadow Realm role"
        )
    
        await ctx.send(embed=modem)

"""
    @commands.slash_command(name="help", description="Need help?")
    @cooldown(1, 10, BucketType.user)
    async def help(self, ctx):

        prefix = "!"
        embed = disnake.Embed(
            title="Help Dialog",
            description=f"Developer: <@{owner[0]}\nServer Owner: <@426772465490853888>",
            color=color
        )

        for x in self.bot.cogs:
            cog = self.bot.get_cog(x.lower())
            commands = cog.get_commands()
            data=[]
            for command in commands:
                description=command.description.partition("\n")[0]
                data.append(f"{prefix}{command.name} - {description}")
            help_text = "\n".join(data)
            embed.add_field(
                name=x.captitalize(),
                value=f"`{help_text}`",
                inline=False
            )
            await ctx.send(embed=embed)
"""

def setup(bot):
    bot.add_cog(HelpMenu(bot))