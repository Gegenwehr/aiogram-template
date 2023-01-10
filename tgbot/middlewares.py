from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from tgbot.database.commands import AddCommands, UpdateCommands


class DbMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        user = await AddCommands.user(user=message.from_user,
                                      check_availability=True)

        update_sql_data = {}
        if user.username != message.from_user.username:
            update_sql_data['username'] = message.from_user.username
        if user.full_name != message.from_user.full_name:
            update_sql_data['full_name'] = message.from_user.full_name

        if update_sql_data:
            await UpdateCommands.user(user, **update_sql_data)

        data['user'] = user
