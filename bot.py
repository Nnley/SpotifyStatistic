import asyncio

from loader import dp, bot
from handlers.user.start import register_start
from handlers.user.auth import register_auth
from handlers.user.help import register_help
from handlers.user.change_language import register_change_language
from handlers.user.stats import register_stats
from handlers.inline_handler import register_inline

from keyboards.default_commands import set_default_commands, remove_default_commands

def register_all_handlers(dp):
    register_start(dp)
    register_auth(dp)
    register_help(dp)
    register_change_language(dp)
    register_inline(dp)
    register_stats(dp)

async def main():
    register_all_handlers(dp)
    await set_default_commands(bot)

    try:
        await dp.start_polling()
    finally:
        await remove_default_commands(bot)
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close() # type: ignore


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')