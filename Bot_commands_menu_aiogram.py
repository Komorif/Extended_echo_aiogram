from aiogram.utils import executor

import logging
from aiogram import Bot, Dispatcher, types, executor


from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, callback_query

# Объекты для команд бота
from aiogram.types import BotCommand, BotCommandScopeChat


TOKEN = "5989508618:AAEvFe652Jk836TpS14p9JP4raf0BuapRdo"
logging.basicConfig(level=logging.INFO)


# прокси
proxy_url = "http://proxy.server:3128"


bot = Bot(token=TOKEN, proxy=proxy_url)
dp = Dispatcher(bot)


# Функция (запуск бота)
async def on_startup(dp):
	await bot.send_message(1727165738, "Я запустился")

# Функция (выключение бота)
async def on_shutdown(dp):
	await bot.send_message(1727165738, "Я завершил работу")


# Менюшка команд бота
async def set_starting_commands(bot: Bot, chat_id: int):
	return await bot.set_my_commands(
		commands=[
		BotCommand("start", "Выбор языка"), # /start
		BotCommand("help", "Что я могу?"), # /help
		BotCommand("id", "Узнать свой id"), # /id
		BotCommand("games", "Узнать какие есть игры"), # /games
		BotCommand("echo", "Эхо"), # /echo
		],
		scope=BotCommandScopeChat(chat_id),
		language_code="ru"
	)


# /start
# 1 меню выбор языка
@dp.message_handler(commands="start")
async def command_start(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=menu_one, caption="🇺🇸 / 🇷🇺", reply_markup=mainMenu_en_rus)
    await set_starting_commands(bot, message.from_user.id)


# /help
@dp.message_handler(commands="help")
async def command_help(message: types.Message):
	await message.answer("You can use me for download games, see our Youtube, Discord etc. / Вы можете использовать меня для загрузки игр, посмотреть наш Youtube, Discord и т.д.😲")


# /id
@dp.message_handler(commands="id")
async def command_id(message: types.Message):
	await message.answer(f"Ваш id: {message.from_user.id}")


# /games
@dp.message_handler(commands="games")
async def command_games(message: types.Message):
	await message.answer("ANDROID\n1. Cars\n2. Mosaic\n\nPC\n1. Horror\n2. ES MOD\n\nWEB GAMES\nNot yet/пока нет")


# /echo
@dp.message_handler(commands="echo")
async def command_echo(message: types.Message):
	await message.answer("Если отправить что-то из этого\n1. Смайлик\n2. Эмоджи\n3. Gif\n4. Видео\n4. Фото\n\nБот отправит вам его в ответ")


# Register dispather
def register_handlers_client(dp : Dispatcher):
  dp.register_message_handler(command_start, commands=["start"])

if __name__ == "__main__":
	executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)