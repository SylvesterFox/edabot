from tortoise import Tortoise
import loggers

async def on_startup():
    loggers.bot.debug('Connecting to database...')
    await Tortoise.init(
        db_url='sqlite://data/db.sqlite3',
        modules={'models': ['bot.database.models']}
    )
    loggers.bot.debug('Connected to database!')

    loggers.bot.debug('Generating database schema...')
    await Tortoise.generate_schemas()
    loggers.bot.debug('Database schema generated successfully!')
