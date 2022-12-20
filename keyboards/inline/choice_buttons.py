from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from calculator_bot_aiogram.keyboards.inline.callback_datas import MyCallback

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [  # 1 row
            InlineKeyboardButton(text="peer", callback_data=MyCallback(text="peer", value=1).pack()),
            InlineKeyboardButton(text="apples", callback_data=MyCallback(text="apples", value=42).pack()),
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
