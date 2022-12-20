from loader import bot

if __name__ == "__main__":
    from handlers import dp

    dp.run_polling(bot)
