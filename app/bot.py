import logging

from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

