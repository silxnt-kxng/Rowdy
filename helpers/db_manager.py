import os
import aiosqlite

DATABASE_PATH = f"{os.path.realpath(os.path.dirname(__file__))}/Rowdy/database/database.db"

async def get_blacklisted_users() -> list:
    """
    This will return all users that are blacklisted.
    
    :return: The list of blacklisted users
    """

    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute(
            "SELECT user_id, strftime('%s', created_at) FROM blacklist"
        ) as cursor:
            result = await cursor.fetchall()
            return result
        
async def is_blacklisted(user_id: int) -> bool:
    """
    This function checks if a user is blacklisted.
    
    :param user_id: The ID of the user that should be checked.
    :return: True if the user is blacklisted, False if not"""

    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute(
            "SELFECT * FROM blacklist WHERE user_id=?", (user_id,)
        ) as cursor:
            result = await cursor.fetchone()
            return result is not None
        
async def add_user_to_blacklist(user_id: int) -> int:
    """
    This function adds a user to the blacklist based on their ID
    
    :param user_id: The ID of the user to be added to the blacklist
    """

    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("INSERT INTO blacklist(user_id) VALUE (?)", (user_id,))
        await db.commit()
        rows = await db.execute("SELECT COUNT(*) FROM blacklist")
        async with rows as cursor:
            result = await cursor.fetchone()
            return result[0] if result is not None else 0

async def remove_user_from_blacklist(user_id: int) -> int:
    """
    This function removes a user from the blacklist based on their ID
    
    :param user_id: The ID of the user to be removed from the blacklist
    """

    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("DELETE FROM blacklist WHERE user_id=?", (user_id,))
        await db.commit()

async def add_warn(user_id: int, server_id: int, moderator_id: int, reason: str) -> int:
    """
    This fucntion will add a warn to the database for the user.
    
    :param user_id: The ID of the user tha should be warned.
    :param reason: The reason why the user should be warned.
    """

    async with aiosqlite.connect(DATABASE_PATH) as db:
        rows = await db.execute(
            "SELECT id FROM warns WHERE user_id=? AND server_id=? ORDER BY id DESC LIMIT 1",
            (
                user_id,
                server_id,
            ),
        )
        async with rows as cursor:
            result = await cursor.fetchone()
            warn_id = result[0] + 1 if result is not None else 1
            await db.execute(
                "INSERT INTO warns(id, user_id, server_id, moderator_id, reason) VALUES (?, ?, ?, ?, ?)",
                (
                    warn_id,
                    user_id,
                    server_id,
                    moderator_id,
                    reason,
                ),
            )
            await db.commit()
            return warn_id
    
async def remove_warn(warn_id: int, user_id: int, server_id: int) -> int:
    """
    This function removes a warn for the user.
    
    :param warn_id: The ID of the warn.
    :param user_id: The ID of the user that was wanred.
    :param server_id: The ID of the server where the user has been warned.
    """
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute(
            "DELETE FROM warns WHERE id=? AND user_id=? AND server_id=?",
            (
                warn_id,
                user_id,
                server_id,
            ),
        )
        await db.commit()
        rows = await db.execute(
            "SELECT COUNT(*) FROM warns WHERE user_id=? AND server_id=?",
            (
                user_id,
                server_id,

            ),
        )
        async with rows as cursor