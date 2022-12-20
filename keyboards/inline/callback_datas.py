from aiogram.filters.callback_data import CallbackData


class MyCallback(CallbackData, prefix="my"):
    text: str
    value: int


class Operation(CallbackData, prefix="op"):
    text: str
