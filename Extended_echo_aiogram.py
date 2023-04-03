from aiogram.utils import executor

import logging
from aiogram import Bot, Dispatcher, types, executor


from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, callback_query

# Объекты для команд бота
from aiogram.types import BotCommand, BotCommandScopeChat


TOKEN = "your token"
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



# Продвинутое эхо
@dp.message_handler(content_types=[
	types.ContentType.DOCUMENT, types.ContentType.PHOTO,
	types.ContentType.STICKER, types.ContentType.VIDEO,
	types.ContentType.TEXT,  types.ContentType.ANIMATION,
	types.ContentType.VOICE
])
async def download_doc(message: types.Message):
    # Если (документ) работает также с gif
	if 'document' in message:
		await message.answer_document(message.document.file_id)

		# Необязательная загрузка
		#await message.document.download()

	# Если (фото)
	elif 'photo' in message:
		await message.answer_photo(message.photo[-1].file_id)

		# Необязательная загрузка
		#await message.photo[-1].download()

	# Если (стикер)
	elif "sticker" in message:
		await message.answer_sticker(message.sticker.file_id)

		# Необязательная загрузка
		#await message.sticker.download()

	# Если (видео)
	elif "video" in message:
		await message.answer_video(message.video.file_id)

		# Необязательная загрузка
		#await message.video.download()

	# Если (какой - либо текст) работает также со смайликами
	elif "text" in message:
	    await message.answer(message.text)

	# Если (голосовое сообщение)
	elif "voice" in message:
	    await message.answer_voice(message.voice.file_id)

	    # Необязательная загрузка
	    #await message.voice.download()



# Register dispather
def register_handlers_client(dp : Dispatcher):
  dp.register_message_handler(command_start, commands=["start"])

if __name__ == "__main__":
	executor.start_polling(dp)