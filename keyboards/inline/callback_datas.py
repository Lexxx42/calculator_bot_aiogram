from aiogram.filters.callback_data import CallbackData


class MyCallback(CallbackData, prefix="my"):
    text: str
    value: int


# buy_callback = MyCallback(
#     text="", value=0
# )

# buy_callback = CallbackData()
# "buy", "item_name", "quantity"
# 1 - тип, 2 - что сохранить в кнопке
# "buy:item_name:2"
# CallbackData()
