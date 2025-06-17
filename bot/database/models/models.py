from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.UUIDField(pk=True, auto_increment=False)
    telegram_id = fields.BigIntField()
    username = fields.CharField(max_length=255, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)