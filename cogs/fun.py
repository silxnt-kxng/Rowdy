import aiohttp
import disnake
from disnake.ext import commands
from disnake.ext.commands import slash_command
from disnake.ext.commands.cooldowns import BucketType
from disnake.ext.commands.core import cooldown


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="kick", description="Kick someone or yourself in the shins")
    @cooldown(1, 60, BucketType.member)
    async def kick(self, ctx, member : disnake.Member):
        if not member:
                await ctx.send("You kicked yourself in the shin (ouch)")
        
        else:
                await ctx.send(f"You kicked {member.name} in the shins (ouch)")
    
    @commands.slash_command(name="hug", description="Hug somone or yourself")
    @cooldown(1, 60, BucketType.member)
    async def hug(self, ctx, member : disnake.Member):
        if not member:
            await ctx.send("You hugged yourself...")
        
        else:
            await ctx.send(f"You hugged {member.name}. Aww.")
    
    @commands.slash_command(name="dadjoke", description="Want a dad joke?")
    @cooldown(1, 60, BucketType.member)
    async def dadjoke(self, ctx):
        api = "https://icanhazdadjoke.com/"
        async with aiohttp.request("GET", api, headers={"Accept": "text/plain"}) as r:
            result = await r.text(encoding="UTF-8")
        
        await ctx.send(f"`{result}`")
    
def setup(bot):
    bot.add_cog(Fun(bot))