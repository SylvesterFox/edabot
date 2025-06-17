from aiogram import Dispatcher
import loggers
from . import message, callback_query  

def setup(*, dispatcher: Dispatcher):
    loggers.bot.debug('Setup handler')
    message.setup(dispatcher=dispatcher)
    callback_query.setup(dispatcher=dispatcher)
