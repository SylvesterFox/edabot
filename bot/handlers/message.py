from aiogram import Dispatcher, Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from bot.template import message_template, inlinekeyboard
from bot.database.repo import RepoUser

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message, Admin_id: int):
    await RepoUser.UserRepository.creating_user(message, Admin_id)
    photo_path = FSInputFile('public/1080x1080-1.jpg')
    await message.answer_photo(photo=photo_path)
    await message.answer(message_template.start_message, parse_mode='html', reply_markup=inlinekeyboard.keyboard_start)

@router.message(Command('get_db'))
async def cmd_get_db(message: Message, Admin_id: int):
    if message.from_user.id == Admin_id:
        await message.answer_document(FSInputFile('db.sqlite3'))

def setup(*, dispatcher: Dispatcher):
    dispatcher.include_router(router)