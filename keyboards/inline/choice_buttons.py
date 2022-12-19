from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from calculator_bot_aiogram.keyboards.inline.callback_datas import buy_callback


choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [  # 1 row
            InlineKeyboardButton(text="peer", callback_data=buy_callback.new(
                item_name="pear", quantity=1
            )),
            InlineKeyboardButton(text="apples", callback_data="buy:apple:5"),
        ],
        [  # 2 row
            InlineKeyboardButton(text="abort", callback_data="cancel")
        ]
    ]
)
