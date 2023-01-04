from typing import Union

from aiogram import types
from gino.schema import GinoSchemaVisitor

from .models import Users
from .models import db
from ..config import load_config

config = load_config('.env', db=True)


class GetCommands:
    @staticmethod
    async def user(user_id: Union[str, int]) -> Users:
        user = await Users.query.where(Users.user_id == user_id).gino.first()
        return user


class AddCommands:
    @staticmethod
    async def user(user: types.User,
                   check_availability: bool = False) -> Users:
        # Получить user ID из Context Var
        if not user:
            user = types.User.get_current()

        if check_availability:
            old_user = await GetCommands.user(user.id)
            if old_user:
                return old_user

        new_user = Users(
            user_id=user.id,
            username=user.username,
            full_name=user.full_name
        )
        await new_user.create()
        return new_user


class UpdateCommands:
    @staticmethod
    async def user(user: Users,
                   **params) -> Users:
        return await user.update(**params).apply()


async def go_db(recreate: bool = False) -> None:
    await db.set_bind(f'postgresql://{config.user}:{config.password}@{config.host}/{config.database}')
    db.gino: GinoSchemaVisitor
    if recreate:
        await db.gino.drop_all()
        await db.gino.create_all()
