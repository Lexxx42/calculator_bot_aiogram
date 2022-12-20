import logging

from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, Update

from calculator_bot_aiogram.keyboards.inline.callback_datas import MyCallback
from calculator_bot_aiogram.keyboards.inline.choice_buttons import choice
from calculator_bot_aiogram.loader import dp

ENTERED_DATA = ''
ANSWER = ""


@dp.message(Command("start"))
async def show_items(message: Message):
    await message.answer(text="Simple calculator", reply_markup=choice)


@dp.callback_query(MyCallback.filter(F.text == "1"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    global ENTERED_DATA, ANSWER
    await call.answer(cache_time=1)
    logging.info(f"call = {callback_data}")
    ENTERED_DATA += callback_data.text
    ANSWER = await call.message.answer(text=f"Entered number = {ENTERED_DATA}")
    if ENTERED_DATA != "":
        await ANSWER.edit_text(text="suka")
