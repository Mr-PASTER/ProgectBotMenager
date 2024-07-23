from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart


rt = Router()


@rt.message(CommandStart)
async def start(message: Message):
    await message.answer(message.text)
