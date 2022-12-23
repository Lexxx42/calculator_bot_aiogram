import logging
from calculator_bot_aiogram.loader import bot
from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from calculator_bot_aiogram.calc.controller import send_to_controller
from calculator_bot_aiogram.keyboards.inline.callback_datas import MyCallback, Operation
from calculator_bot_aiogram.keyboards.inline.choice_buttons import choice
from calculator_bot_aiogram.loader import dp

IS_FUNCTION_ADDED = False
ENTERED_DATA = ''
ANSWER = ""
MESSAGE = "Input: "
IS_FIRST_MESSAGE = True


@dp.message(Command("start"))
async def show_items(message: Message):
    global IS_FUNCTION_ADDED, ENTERED_DATA, ANSWER, MESSAGE, IS_FIRST_MESSAGE
    IS_FUNCTION_ADDED, ENTERED_DATA, ANSWER, MESSAGE, IS_FIRST_MESSAGE = (False, "", "", "Input: ", True)
    await message.answer(text="Simple calculator. Working with <b>two</b> numbers.", reply_markup=choice)


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
async def my_callback_foo(call: CallbackQuery, callback_data: Operation):
    global IS_FUNCTION_ADDED
    if not IS_FUNCTION_ADDED and ENTERED_DATA != "":
        IS_FUNCTION_ADDED = True
        await sent_callback_data(call, callback_data.text)
    else:
        await call.answer(cache_time=1)


@dp.callback_query(Operation.filter(F.text == " - "))
async def my_callback_foo(call: CallbackQuery, callback_data: Operation):
    global IS_FUNCTION_ADDED
    if not IS_FUNCTION_ADDED and ENTERED_DATA != "":
        IS_FUNCTION_ADDED = True
        await sent_callback_data(call, callback_data.text)
    else:
        await call.answer(cache_time=1)


@dp.callback_query(Operation.filter(F.text == " * "))
async def my_callback_foo(call: CallbackQuery, callback_data: Operation):
    global IS_FUNCTION_ADDED
    if not IS_FUNCTION_ADDED and ENTERED_DATA != "":
        IS_FUNCTION_ADDED = True
        await sent_callback_data(call, callback_data.text)
    else:
        await call.answer(cache_time=1)


@dp.callback_query(Operation.filter(F.text == " / "))
async def my_callback_foo(call: CallbackQuery, callback_data: Operation):
    global IS_FUNCTION_ADDED
    if not IS_FUNCTION_ADDED and ENTERED_DATA != "":
        IS_FUNCTION_ADDED = True
        await sent_callback_data(call, callback_data.text)
    else:
        await call.answer(cache_time=1)


@dp.callback_query(Operation.filter(F.text == " // "))
async def my_callback_foo(call: CallbackQuery, callback_data: Operation):
    global IS_FUNCTION_ADDED
    if not IS_FUNCTION_ADDED and ENTERED_DATA != "":
        IS_FUNCTION_ADDED = True
        await sent_callback_data(call, callback_data.text)
    else:
        await call.answer(cache_time=1)


@dp.callback_query(Operation.filter(F.text == "."))
async def my_callback_foo(call: CallbackQuery, callback_data: Operation):
    input_list = ENTERED_DATA.split()
    if ENTERED_DATA == "":
        await call.answer(cache_time=1)
    else:
        if "." not in input_list[0]:
            await call.answer(cache_time=1)
            await sent_callback_data(call, callback_data.text)
        elif '.' in input_list[0] and "." not in input_list[len(input_list) - 1]:
            await call.answer(cache_time=1)
            await sent_callback_data(call, callback_data.text)


@dp.callback_query(Operation.filter(F.text == " % "))
async def my_callback_foo(call: CallbackQuery, callback_data: Operation):
    global IS_FUNCTION_ADDED
    if not IS_FUNCTION_ADDED and ENTERED_DATA != "":
        IS_FUNCTION_ADDED = True
        await sent_callback_data(call, callback_data.text)
    else:
        await call.answer(cache_time=1)


@dp.callback_query(Operation.filter(F.text == " pow "))
async def my_callback_foo(call: CallbackQuery, callback_data: Operation):
    global IS_FUNCTION_ADDED
    if not IS_FUNCTION_ADDED and ENTERED_DATA != "":
        IS_FUNCTION_ADDED = True
        await sent_callback_data(call, callback_data.text)
    else:
        await call.answer(cache_time=1)


@dp.callback_query(Operation.filter(F.text == "H"))
async def my_callback_foo(call: CallbackQuery, callback_data: Operation):
    if ENTERED_DATA != "":
        logging.info(f"call = {callback_data}")
        await sent_callback_data(call, callback_data.text)
    else:
        await call.answer(cache_time=1)


@dp.callback_query(Operation.filter(F.text == "C"))
async def my_callback_foo(call: CallbackQuery, callback_data: Operation):
    if ENTERED_DATA != "":
        logging.info(f"call = {callback_data}")
        await sent_callback_data(call, callback_data.text)
    else:
        await call.answer(cache_time=1)


@dp.callback_query(Operation.filter(F.text == "+/-"))
async def my_callback_foo(call: CallbackQuery, callback_data: Operation):
    if ENTERED_DATA != "":
        logging.info(f"call = {callback_data}")
        await sent_callback_data(call, callback_data.text)
    else:
        await call.answer(cache_time=1)


@dp.callback_query(Operation.filter(F.text == "="))
async def my_callback_foo(call: CallbackQuery, callback_data: Operation):
    if len(ENTERED_DATA.split()) < 3:
        await call.answer(cache_time=1)
    else:
        logging.info(f"call = {callback_data}")
        await sent_callback_data(call, callback_data.text)


async def sent_callback_data(call, callback_data_text):
    global ENTERED_DATA, ANSWER, MESSAGE, IS_FIRST_MESSAGE, IS_FUNCTION_ADDED
    await call.answer(cache_time=1)
    logging.info(f"call = {callback_data_text}")
    if ENTERED_DATA != "" and callback_data_text == "=":
        user_input = ENTERED_DATA.split()
        await call.answer(cache_time=1)
        try:
            first_number = float(user_input[0])
            logging.info(f"first_number = {first_number}")
            second_number = float(user_input[2])
            logging.info(f"second_number = {second_number}")
        except ValueError as e:
            logging.info(f"ValueError = {e}")
            await ANSWER.edit_text(text="Input data is incorrect")
            logging.info(f"ANSWER = {ANSWER}")
            await error(ANSWER)
            return
        if second_number == 0 and user_input[1] in ['/', '//', '%']:
            await ANSWER.edit_text(text="Division or modulo by zero")
            await error(ANSWER)
            logging.info(f"error = {ANSWER}")
        else:
            controller_answer = send_to_controller(user_input[0], user_input[1], user_input[2])
            logging.info(f"data sent to controller = {(user_input[0], user_input[1], user_input[2])}")
            logging.info(f"controller answer = {controller_answer}")
            MESSAGE = "Return = "
            MESSAGE += controller_answer
            logging.info(f"new MESSAGE = {MESSAGE}")
            logging.info(f"new ANSWER = {ANSWER}")
            await ANSWER.edit_text(text=MESSAGE)
            await call.answer(cache_time=1)
            await error(ANSWER)
    elif ENTERED_DATA != "" and callback_data_text == "H":
        logging.info(f"call = {callback_data_text}")
        ENTERED_DATA = ENTERED_DATA.strip()[:-1]
        logging.info(f"new ENTERED_DATA = {ENTERED_DATA}")
        MESSAGE = "Input: "
        MESSAGE += ENTERED_DATA
        logging.info(f"new MESSAGE = {MESSAGE}")
        logging.info(f"new ANSWER = {ANSWER}")
        if callback_data_text not in ["+", "-", "/", "//", "%", "pow", "*"]:
            IS_FUNCTION_ADDED = False
        await ANSWER.edit_text(text=MESSAGE)
    elif ENTERED_DATA != "" and callback_data_text == "C":
        logging.info(f"call = {callback_data_text}")
        ENTERED_DATA = ""
        logging.info(f"new ENTERED_DATA = {ENTERED_DATA}")
        MESSAGE = "Input: "
        logging.info(f"new MESSAGE = {MESSAGE}")
        logging.info(f"new ANSWER = {ANSWER}")
        IS_FUNCTION_ADDED = False
        await ANSWER.edit_text(text=MESSAGE)
    elif ENTERED_DATA != "" and callback_data_text == "+/-":
        logging.info(f"call = {callback_data_text}")
        data_list = ENTERED_DATA.split()
        if len(data_list) < 2:
            ENTERED_DATA = str(float(data_list[0]) * -1)
            logging.info(f"new ENTERED_DATA = {ENTERED_DATA}")
            temp_message = MESSAGE.split()
            temp_message[1] = ENTERED_DATA
            MESSAGE = ' '.join(temp_message)
            logging.info(f"new MESSAGE = {MESSAGE}")
            logging.info(f"new ANSWER = {ANSWER}")
            temp = MESSAGE.split()
            ENTERED_DATA = temp[1]
            logging.info(f"new ANSWER = {ENTERED_DATA}")
            await ANSWER.edit_text(text=MESSAGE)
        elif len(data_list) == 2:
            ENTERED_DATA = str(float(data_list[0]) * -1)
            logging.info(f"new ENTERED_DATA = {ENTERED_DATA}")
            temp_message = MESSAGE.split()
            temp_message[1] = ENTERED_DATA
            MESSAGE = ' '.join(temp_message) + ' '
            logging.info(f"new MESSAGE = {MESSAGE}")
            logging.info(f"new ANSWER = {ANSWER}")
            temp = MESSAGE.split()
            ENTERED_DATA = temp[1]
            logging.info(f"new ANSWER = {ENTERED_DATA}")
            await ANSWER.edit_text(text=MESSAGE)
        elif len(data_list) == 3:
            ENTERED_DATA = str(float(data_list[2]) * -1)
            logging.info(f"new ENTERED_DATA = {ENTERED_DATA}")
            temp_message = MESSAGE.split()
            temp_message[3] = ENTERED_DATA
            MESSAGE = ' '.join(temp_message)
            logging.info(f"new MESSAGE = {MESSAGE}")
            logging.info(f"new ANSWER = {ANSWER}")
            temp = MESSAGE.split()
            ENTERED_DATA = temp[1] + ' ' + temp[2] + ' ' + temp[3]
            logging.info(f"new ANSWER = {ENTERED_DATA}")
            await ANSWER.edit_text(text=MESSAGE)
    elif ENTERED_DATA != "" and callback_data_text != "H":
        ENTERED_DATA += callback_data_text
        logging.info(f"new ENTERED_DATA = {ENTERED_DATA}")
        MESSAGE += callback_data_text
        await ANSWER.edit_text(text=MESSAGE)
        logging.info(f"new MESSAGE = {MESSAGE}")
        logging.info(f"answer edit = {ANSWER}")
    elif ENTERED_DATA == "" and IS_FIRST_MESSAGE:
        ENTERED_DATA += callback_data_text
        logging.info(f"new ENTERED_DATA = {ENTERED_DATA}")
        MESSAGE += callback_data_text
        logging.info(f"new MESSAGE = {MESSAGE}")
        ANSWER = await call.message.answer(text=MESSAGE)
        logging.info(f"new ANSWER = {ANSWER}")
        IS_FIRST_MESSAGE = False
    elif ENTERED_DATA == "" and not IS_FIRST_MESSAGE:
        ENTERED_DATA += callback_data_text
        logging.info(f"new ENTERED_DATA = {ENTERED_DATA}")
        MESSAGE += callback_data_text
        logging.info(f"new MESSAGE = {MESSAGE}")
        await ANSWER.edit_text(text=MESSAGE)
        logging.info(f"new ANSWER = {ANSWER}")
        IS_FIRST_MESSAGE = False


@dp.message()
async def error(message):
    global ENTERED_DATA, ANSWER, MESSAGE, IS_FIRST_MESSAGE, IS_FUNCTION_ADDED
    IS_FUNCTION_ADDED = False
    ENTERED_DATA = ''
    ANSWER = ""
    MESSAGE = "Input: "
    IS_FIRST_MESSAGE = True
    await bot.send_message(message.chat.id, """use /start to use bot and to create a new calc instance.
input works only from inline keyboard.""")
