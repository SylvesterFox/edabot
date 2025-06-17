import uuid
from aiogram.types import Message
from bot.database.models import User
import loggers

class UserRepository:
    @staticmethod
    async def creating_user(message: Message):
        uuid_user = uuid.uuid4()
        user, created = await User.get_or_create(
            telegram_id=message.from_user.id,
            defaults={
                "username": message.from_user.username,
                "id": uuid_user
            }
        )

        if created:
            loggers.bot.info(f"New user created: {user.username} - {user.telegram_id} - {user.id}")