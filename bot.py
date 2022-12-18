import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import Message
from TOKEN import t

TOKEN = t
dp = Dispatcher()

logger = logging.getLogger(__name__)


@dp.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b> This is a calculator bot.")


def main() -> None:
    # Initialize Bot instance with an default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode="HTML")
    # And the run events dispatching
    dp.run_polling(bot)


@dp.message(Command(commands=["reply_builder"]))
async def reply_builder(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 10):
        builder.add(types.KeyboardButton(text=str(i)))
    builder.add(types.KeyboardButton(text='switch type'))
    builder.add(types.KeyboardButton(text='sum'))
    builder.add(types.KeyboardButton(text='sub'))
    builder.add(types.KeyboardButton(text='div'))
    builder.add(types.KeyboardButton(text='mult'))
    builder.add(types.KeyboardButton(text='pow'))
    builder.adjust(4)
    await message.answer(
        "Выберите число:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )


@dp.message(Command(commands=["help"]))
async def command_help_handler(message: Message) -> None:
    """
    This handler receive messages with `/help` command
    """
    await message.answer("""
List of available commands:
/start - bot info
/help - help
/reply_builder - show calculator
""")


# сделать режимы работы, если режим не выбран, то запускаем этот метод
# @dp.message()
# async def echo_handler(message: types.Message) -> None:
#     """
#     Handler will forward received message back to the sender
#
#     By default, message handler will handle all message types (like text, photo, sticker and etc.)
#     """
#     try:
#         # Send copy of the received message
#
#         await message.answer("""
# List of available commands:
# /start - bot info
# /reply_builder - show calculator
# """)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")


if __name__ == "__main__":
    main()
