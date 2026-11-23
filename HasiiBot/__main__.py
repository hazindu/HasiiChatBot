import asyncio
import importlib

# Ensure an event loop is set for Python 3.10+ before pyrogram import
try:
    asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from pyrogram import idle

from HasiiBot import LOGGER, app
from HasiiBot.modules import ALL_MODULES


async def jarvis_boot():
    try:
        await app.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("HasiiBot.modules." + all_module)

    LOGGER.info(f"@{app.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(jarvis_boot()) 
    LOGGER.info("Stopping app Bot...")
