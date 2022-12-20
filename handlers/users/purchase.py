from aiogram.filters import Command
from aiogram.types import Message

from calculator_bot_aiogram.keyboards.inline.choice_buttons import choice
from calculator_bot_aiogram.loader import dp


@dp.message(Command("items"))
async def show_items(message: Message):
    await message.answer(text="1st string. \n"
                              "second string",
                         reply_markup=choice)
