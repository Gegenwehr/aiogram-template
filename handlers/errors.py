import logging

from aiogram import Dispatcher, types


async def error_handler(update: types.Update, exception):
    logging.getLogger('aiogram').error(f'Update: {update}\nError: {exception}')


def register_errors(dp: Dispatcher):
    dp.register_errors_handler(error_handler)