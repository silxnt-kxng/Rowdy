import asyncio
import json
import logging
import os
import platform
import random
import sys
import traceback

import aiosqlite
import disnake
from disnake.ext import commands, tasks
from disnake.ext.commands import when_mentioned_or

owner = [422835542653272066, 951235151860486175]
intents = disnake.Intents.all()


bot = commands.Bot(
    command_prefix=when_mentioned_or,
    intents=intents,
    owner_ids=owner,
    description="It's something",
    help_command=None,
    sync_commands_on_cog_unload=True
    )

def fancy_traceback(exc: Exception) -> str:
    """May not fit the message content limit"""
    text = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    return f"```py\n{text[-4086:]}\n```"

@bot.event
async def on_ready():
        print("--------")
        print(
            f"\n"
            f"The bot is ready.\n"
            f"User: {bot.user}\n"
            f"ID: {bot.user.id}\n"
        )


print("Starting rotating statuses...")

@tasks.loop(seconds=60)
async def statuschange():
        await bot.wait_until_ready()

        status = [
                "with Alex's sanity!",
                "with you!",
                "Mario Kart 8!",
                "Hearthstone!",
                "Smash Bros Ultimate!",
                "NBA 2K22!",
                "Madden!",
                "Overwatch 2!",
                "with Alex's hard drive!"
                "/help"
                ]

        statuschoice = random.choice(status)
        await bot.change_presence(status=disnake.Status.online, activity=disnake.Game(statuschoice))
        
statuschange.start()
print(" Rotating status enabled.")

extentions = [
        'cogs.help',
        'cogs.fun',
        'cogs.general',
        'cogs.moderate'
        #'cogs.error'
        ]

print("Loading cogs...")

if __name__ == '__main__':
    for ext in extentions:
        bot.load_extension(ext)
        print(f"  {ext} loaded.")

print("Cogs loaded. Bot starting.")
print(bot.owner_ids)
print(bot.description)
bot.run("OTcxMDkwNTk2NDQ4MDUxMjIw.GkUm88.3MaEkOm7yZmMHEzm4N3TXx0dWrP6Pc4nEkR__k")