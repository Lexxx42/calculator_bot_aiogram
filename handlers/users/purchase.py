import logging

from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, Update

from calculator_bot_aiogram.keyboards.inline.callback_datas import MyCallback, Operation
from calculator_bot_aiogram.keyboards.inline.choice_buttons import choice
from calculator_bot_aiogram.loader import dp

IS_FUNCTION_ADDED = False
ENTERED_DATA = ''
ANSWER = ""
MESSAGE = "Input: "


@dp.message(Command("start"))
async def show_items(message: Message):
    global IS_FUNCTION_ADDED, ENTERED_DATA, ANSWER, MESSAGE
    IS_FUNCTION_ADDED, ENTERED_DATA, ANSWER, MESSAGE = (False, "", "", "Input: ")
    await message.answer(text=f"Simple calculator. Working with <b>two</b> numbers.", reply_markup=choice)


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


@dp.callback_query(Operation.filter(F.text == " + "))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    global IS_FUNCTION_ADDED
    if "+" not in ENTERED_DATA and not IS_FUNCTION_ADDED:
        IS_FUNCTION_ADDED = True
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == " - "))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    global IS_FUNCTION_ADDED
    if "-" not in ENTERED_DATA and not IS_FUNCTION_ADDED:
        IS_FUNCTION_ADDED = True
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == " * "))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    global IS_FUNCTION_ADDED
    if "*" not in ENTERED_DATA and not IS_FUNCTION_ADDED:
        IS_FUNCTION_ADDED = True
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == " / "))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    global IS_FUNCTION_ADDED
    if "/" not in ENTERED_DATA and not IS_FUNCTION_ADDED:
        IS_FUNCTION_ADDED = True
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == " // "))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    global IS_FUNCTION_ADDED
    if "//" not in ENTERED_DATA and not IS_FUNCTION_ADDED:
        IS_FUNCTION_ADDED = True
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == "."))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    input_list = ENTERED_DATA.split()
    if "." not in input_list[0]:
        await sent_callback_data(call, callback_data.text)
    elif '.' in input_list[0] and "." not in input_list[len(input_list) - 1]:
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == " % "))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    global IS_FUNCTION_ADDED
    if "%" not in ENTERED_DATA and not IS_FUNCTION_ADDED:
        IS_FUNCTION_ADDED = True
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == " pow "))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    global IS_FUNCTION_ADDED
    if "pow" not in ENTERED_DATA and not IS_FUNCTION_ADDED:
        IS_FUNCTION_ADDED = True
        await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == " sqrt "))
async def my_callback_foo(call: CallbackQuery, callback_data: MyCallback):
    global IS_FUNCTION_ADDED
    if "sqrt" not in ENTERED_DATA and not IS_FUNCTION_ADDED:
        IS_FUNCTION_ADDED = True
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
