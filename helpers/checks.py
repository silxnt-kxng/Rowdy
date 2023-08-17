import json
import os
from typing import Callable, TypeVar

from disnake.ext import commands
from exceptions import *
from helpers import db_manager

T = TypeVar("T")


def is_owner() -> Callable[[T], T]:
    """
    Custom check to see if the user executing the command is an owner
    """
    async def predicate(ctx) -> bool:
        with open(
            f"{os.path.realpath(os.path.dirname(__file__))}/config.json"
        ) as file:
            data = json.load(file)
        if ctx.author.id not in data["owners"]:
            raise UserNotOwner
        return True
    
    return commands.check(predicate)

def not_blacklisted() -> Callable[[T], T]:
    """
    Just like the above.
    Custom check to see if the user executing the command is blacklisted
    """

    async def predicate(ctx) -> bool:
        if await db_manager.is_blacklisted(ctx.author.id):
            raise UserBlacklisted
        
        return True
    
    return commands.check(predicate)