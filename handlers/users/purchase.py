import logging

from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, Update

from calculator_bot_aiogram.keyboards.inline.callback_datas import MyCallback, Operation
from calculator_bot_aiogram.keyboards.inline.choice_buttons import choice
from calculator_bot_aiogram.loader import dp

ENTERED_DATA = ''
ANSWER = ""
MESSAGE = "Entered number = "


@dp.message(Command("start"))
async def show_items(message: Message):
    await message.answer(text="Simple calculator", reply_markup=choice)


@dp.callback_query(MyCallback.filter(F.text == "0"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    await sent_callback_data(call, callback_data.text)


@dp.callback_query(MyCallback.filter(F.text == "1"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    await sent_callback_data(call, callback_data.text)


@dp.callback_query(MyCallback.filter(F.text == "2"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    await sent_callback_data(call, callback_data.text)


@dp.callback_query(MyCallback.filter(F.text == "3"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    await sent_callback_data(call, callback_data.text)


@dp.callback_query(MyCallback.filter(F.text == "4"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    await sent_callback_data(call, callback_data.text)


@dp.callback_query(MyCallback.filter(F.text == "5"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    await sent_callback_data(call, callback_data.text)


@dp.callback_query(MyCallback.filter(F.text == "6"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    await sent_callback_data(call, callback_data.text)


@dp.callback_query(MyCallback.filter(F.text == "7"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    await sent_callback_data(call, callback_data.text)


@dp.callback_query(MyCallback.filter(F.text == "8"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    await sent_callback_data(call, callback_data.text)


@dp.callback_query(MyCallback.filter(F.text == "9"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == "+"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    if "+" not in ENTERED_DATA:
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == "-"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    if "-" not in ENTERED_DATA:
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == "*"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    if "*" not in ENTERED_DATA:
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == "/"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    if "/" not in ENTERED_DATA:
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == "//"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    if "//" not in ENTERED_DATA:
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == "."))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    if "." not in ENTERED_DATA:
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == "%"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    if "%" not in ENTERED_DATA:
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == "pow"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    if "pow" not in ENTERED_DATA:
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == "sqrt"))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    if "sqrt" not in ENTERED_DATA:
        await sent_callback_data(call, callback_data.text)


async def sent_callback_data(call, callback_data_text):
    global ENTERED_DATA, ANSWER, MESSAGE
    await call.answer(cache_time=1)
    logging.info(f"call = {callback_data_text}")
    if ENTERED_DATA != "":
        ENTERED_DATA += callback_data_text
        logging.info(f"new ENTERED_DATA = {ENTERED_DATA}")
        MESSAGE += callback_data_text
        await ANSWER.edit_text(text=MESSAGE)
        logging.info(f"new MESSAGE = {MESSAGE}")
        logging.info(f"answer edit = {ANSWER}")
    else:
        ENTERED_DATA += callback_data_text
        logging.info(f"new ENTERED_DATA = {ENTERED_DATA}")
        MESSAGE += callback_data_text
        logging.info(f"new MESSAGE = {MESSAGE}")
        ANSWER = await call.message.answer(text=MESSAGE)
        logging.info(f"new ANSWER = {ANSWER}")
