from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from calculator_bot_aiogram.keyboards.inline.callback_datas import MyCallback

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [  # 1 row
            InlineKeyboardButton(text="peer", callback_data=MyCallback(foo="demo", bar="42").pack()),
            InlineKeyboardButton(text="apples", callback_data=MyCallback(foo="demo", bar="42").pack()),
        ],
        [  # 2 row
            InlineKeyboardButton(text="abort", callback_data="cancel")
        ]
    ]
)
