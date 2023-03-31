from aiogram.filters.callback_data import CallbackData


class MyCallback(CallbackData, prefix="my"):
    text: str


class Operation(CallbackData, prefix="op"):
    text: str
