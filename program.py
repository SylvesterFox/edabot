import asyncio
import loggers
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from bot import handlers
from bot.database import initDB

from settings import config

logger = logging.getLogger(__name__)

async def Main():
    logger.debug("Building bot!")
    await initDB.on_startup()  # Initialize the database
    # Default bot properties
    default_bot_properties = DefaultBotProperties(
        parse_mode=config.PARSE_MODE,
    )

    bot = Bot(token=config.TOKEN[0], default=default_bot_properties)
    dispatcher = Dispatcher()
    handlers.setup(dispatcher=dispatcher)
    logger.debug("Bot built successfully!")

    extra_data = {
        'Admin_id': config.ADMIN_ID
    }
    
    await dispatcher.start_polling(bot, **extra_data)

loggers.setup()

if __name__ == '__main__':
    try:
        asyncio.run(Main())
    except KeyboardInterrupt:
        logger.warning('Stopped!')
else:
    logger.warning('Use: python program.py')
