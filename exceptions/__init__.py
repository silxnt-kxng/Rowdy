from typing import Any, Optional
from disnake.ext import commands

class UserBlacklisted(commands.CheckFailure):
    """
    Self-explanitory...
    Thrown when a blacklisted user tries to run a command in the bot
    Will alert in the logs
    """

    def __init__(self, message="User is blacklisted!"):
        self.message = message
        super().__init__(self.message)

class UserNotOwner(commands.CheckFailure):
    """
    Again, self-explanitory...
    Thrown when a user that is not a bot owner attempts to use an owner-only command
    Will alert in the logs
    """

    def __init__(self, message="User is not an owner of this bot!"):
        self.message = message
        super().__init__(self.message)