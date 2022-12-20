from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from calculator_bot_aiogram.keyboards.inline.callback_datas import MyCallback

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [  # 1 row
            InlineKeyboardButton(text="peer", buy_callback=MyCallback(text="apple", bar="12").pack()),
            InlineKeyboardButton(text="apples", buy_callback=MyCallback(text="pear", value="42").pack()),
        ],
        [  # 2 row
            InlineKeyboardButton(text="abort", callback_data="cancel")
        ]
    ]
)

pear_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="=", callback_data="123")
        ]
    ]
)

apples_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="=", callback_data="123")
        ]
    ]
)
