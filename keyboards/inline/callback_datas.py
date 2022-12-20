from aiogram.filters.callback_data import CallbackData


class MyCallback(CallbackData, prefix="my"):
    foo: str
    bar: int


# buy_callback = MyCallback()
# buy_callback = CallbackData()
# "buy", "item_name", "quantity"
# 1 - тип, 2 - что сохранить в кнопке
# "buy:item_name:2"
CallbackData()
