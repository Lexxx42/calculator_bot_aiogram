from aiogram import Bot, Dispatcher, types
import TOKEN
import logging

bot = Bot(token=TOKEN.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
logging.basicConfig(filename="my_log.log",
                    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )
