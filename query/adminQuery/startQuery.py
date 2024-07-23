from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from random import randint
from aiogram.filters import CommandStart


rt = Router()


@rt.callback_query(F.data == "random_value")
async def send_random_value(callback: CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))
