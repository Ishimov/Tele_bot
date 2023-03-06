import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import dotenv_values

config = dotenv_values('.env')
BOT_TOKEN = config['BOT_TOKEN']

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start (msg: types.Message):
   await msg.answer(f'Я бот Jarvis. Приятно познакомиться, {msg.from_user.first_name}')

@dp.message_handler(commands=['help'])
async def cmd_help(msg: types.Message):
   await msg.answer('Скоро добавлю команды...')


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message) -> None:
   await msg.answer(len(msg.text) - msg.text.count(' '))


if __name__ == '__main__':
   executor.start_polling(dp)