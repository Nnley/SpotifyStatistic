from __future__ import annotations

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

users_commands: dict[str, str] = {
        "start": "Start bot",
        "help": "Show information about bot",
        "stats": "Show your Spotify statistics",
        "auth": "Authorize with Spotify",
}


async def set_default_commands(bot: Bot) -> None:
    await remove_default_commands(bot)

    commands = [
        BotCommand(command=command, description=description)
        for command, description in users_commands.items()
    ]
    
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())

async def remove_default_commands(bot: Bot) -> None:
    await bot.delete_my_commands(scope=BotCommandScopeDefault())