from aiogram import Dispatcher, Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from bot.template import message_template, inlinekeyboard

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    photo_path = FSInputFile('public/1080x1080-1.jpg')
    await message.answer_photo(photo=photo_path)
    await message.answer(message_template.start_message, parse_mode='html', reply_markup=inlinekeyboard.keyboard_start)


def setup(*, dispatcher: Dispatcher):
    dispatcher.include_router(router)