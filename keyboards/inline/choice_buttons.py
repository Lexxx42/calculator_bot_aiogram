from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from calculator_bot_aiogram.keyboards.inline.callback_datas import MyCallback, Operation

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [  # 1 row
            InlineKeyboardButton(text="7", callback_data=MyCallback(text="7").pack()),
            InlineKeyboardButton(text="8", callback_data=MyCallback(text="8").pack()),
            InlineKeyboardButton(text="9", callback_data=MyCallback(text="9").pack()),
            InlineKeyboardButton(text="+/-", callback_data=Operation(text="+/-").pack()),
            InlineKeyboardButton(text="<-", callback_data=Operation(text="H").pack()),
            InlineKeyboardButton(text="C", callback_data=Operation(text="C").pack()),
        ],
        [  # 2 row
            InlineKeyboardButton(text="4", callback_data=MyCallback(text="4").pack()),
            InlineKeyboardButton(text="5", callback_data=MyCallback(text="5").pack()),
            InlineKeyboardButton(text="6", callback_data=MyCallback(text="6").pack()),
            InlineKeyboardButton(text="/", callback_data=Operation(text=" / ").pack()),
            InlineKeyboardButton(text="//", callback_data=Operation(text=" // ").pack()),
            InlineKeyboardButton(text="%", callback_data=Operation(text=" % ").pack()),
        ],
        [  # 3 row
            InlineKeyboardButton(text="1",callback_data=MyCallback(text="1").pack()),
            InlineKeyboardButton(text="2", callback_data=MyCallback(text="2").pack()),
            InlineKeyboardButton(text="3", callback_data=MyCallback(text="3").pack()),
            InlineKeyboardButton(text="*", callback_data=Operation(text=" * ").pack()),
            InlineKeyboardButton(text="-", callback_data=Operation(text=" - ").pack()),
            InlineKeyboardButton(text="pow", callback_data=Operation(text=" pow ").pack()),
        ],
        [  # 4 row
            InlineKeyboardButton(text="0", callback_data=MyCallback(text="0").pack()),
            InlineKeyboardButton(text=",", callback_data=Operation(text='.').pack()),
            InlineKeyboardButton(text="+", callback_data=Operation(text=" + ").pack()),
            InlineKeyboardButton(text="=", callback_data=Operation(text="=").pack()),
        ]
    ]
)
