import logging

from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from calculator_bot_aiogram.keyboards.inline.callback_datas import MyCallback
from calculator_bot_aiogram.keyboards.inline.choice_buttons import choice, pear_keyboard, apples_keyboard
from calculator_bot_aiogram.loader import dp


@dp.message(Command("items"))
async def show_items(message: Message):
    await message.answer(text="1st string. \n"
                              "second string",
                         reply_markup=choice)


@dp.callback_query(MyCallback.filter(F.text == "apple"))
async def buy_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=15)
    logging.info(f"call = {callback_data}")
    quantity = callback_data.get("value")
    await call.message.answer(f"selected appes. Amount = {quantity}",
                              reply_markup=apples_keyboard)


@dp.callback_query(F.text == "pear")
async def buy_pear(call: CallbackQuery):
    await call.answer(cache_time=15)
    callback_data = call.data
    logging.info(f"call = {callback_data}")

    await call.message.answer(text="selected pear",
                              reply_markup=pear_keyboard)
