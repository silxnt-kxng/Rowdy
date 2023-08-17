from unicodedata import name

import disnake
from disnake.ext import commands
from disnake.ext.commands import (MissingPermissions, MissingRequiredArgument,
                                  has_guild_permissions)
from disnake.ext.commands.cooldowns import BucketType
from disnake.ext.commands.core import cooldown

color = disnake.Color.from_rgb(12, 47, 107)

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="giverole", description="Gives someone a role")
    @cooldown(1, 3, BucketType.user)
    @has_guild_permissions(administrator=True)
    async def giverole(self, ctx, user : disnake.Member, *, role : disnake.Role):
        if role in user.roles:
            await ctx.send(f'{user.name} already has the {role} role.')
        else:
            await user.add_roles(role)
            await ctx.send(f'{user.name} has been given the {role} role.')
    
    @giverole.error
    async def giverole_error(ctx, error):
        if isinstance(error, MissingPermissions):
                await ctx.send("You don't have permission to do that.")
                pass
        if isinstance(error, MissingRequiredArgument):
                await ctx.send("You missing one or more required arguements. Add them and try again.")
                pass

    @commands.slash_command(name="removerole", description="Removes a role from someone")
    @cooldown(1, 3, BucketType.user)
    @has_guild_permissions(administrator=True)
    async def removerole(self, ctx, user : disnake.Member, *, role : disnake.Role):
        if role not in user.roles:
            await ctx.send(f'{user.name} doesn\'t have the {role} role.')
        else:
            await user.remove_roles(role)
            await ctx.send(f'{user.name} has been removed from the {role} role.')
    
    @removerole.error
    async def removerole_error(ctx, error):
        if isinstance(error, MissingPermissions):
                await ctx.send("You don't have permission to do that.")
                pass
        if isinstance(error, MissingRequiredArgument):
                await ctx.send("You missing one or more required arguements. Add them and try again.")
                pass

    @commands.slash_command(name="mute", description="Mute someone")
    @cooldown(1, 3, BucketType.user)
    @has_guild_permissions(manage_roles=True)
    async def mute(self, ctx, user : disnake.Member):
        role = disnake.utils.get(ctx.guild.roles, name="SHADOW REALM")
        
        await user.add_role(role)
        await ctx.send(f"Successfully muted {user.mention}.")
        
    @commands.slash_command(name="unmute", description="Unmute someone")
    @cooldown(1, 3, BucketType.user)
    @has_guild_permissions(manage_roles=True)
    async def unmute(self, ctx, user : disnake.Member):
        role = disnake.utils.get(ctx.guild.roles, name="SHADOW REALM")

        await user.remove_roles(role) 
        await ctx.send(f"Successfully unmuted {user.mention}")
    
    @commands.slash_command(name="nick", description="Change someone's nickname")
    @cooldown(1, 10, BucketType.user)
    @has_guild_permissions(manage_nicknames=True)
    async def nick(self, ctx, user: disnake.Member, *, nickname=None):
        try:
            if nickname is not None:
                await user.edit(nick=nickname)
                embed=disnake.Embed(
                    title="Changed Nickname!",
                    description=f"**{user}'s** new nickname is **{nickname}**!",
                    color=color
                    )
                
            else:
                embed=disnake.Embed(
                    title="Changed Nickname!",
                    description=f"**{user}'s** nickname has been reset!",
                    color=color
                )
            await ctx.send(embed=embed)
        
        except:
            embed=disnake.Embed(
                title="Error!",
                description="An error occurred while trying to change the nickname of the user. Make sure my role is above the role of the user you want to change the nickname.",
                color=disnake.Color.red()
            )
            embed.set_thumbnail(url=user.avatar)
        
            await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Moderation(bot))