import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
BOT_TOKEN = '7518402666:AAF-_u9v27wo0ziBFk1Ycb7EJ9fw1T1qpyM'

# URL вашего мини-приложения (должен быть HTTPS)
WEB_APP_URL = 'https://testikppp.github.io/gametest.github.io/'  # Замените на URL вашего мини-приложения

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """Отправляет сообщение с кнопкой для открытия мини-приложения."""
    keyboard = [
        [InlineKeyboardButton("Открыть автокликер", web_app=WebAppInfo(url=WEB_APP_URL))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_text("Нажмите кнопку, чтобы открыть мини-приложение с автокликером:", reply_markup=reply_markup)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    """Отправляет справочное сообщение."""
    await message.reply_text("Я бот, который открывает мини-приложение с автокликером.  Используйте команду /start.")


@dp.callback_query_handler()
async def button_callback(query: types.CallbackQuery):
    """Обрабатывает нажатия на кнопки."""
    # В данном случае, обработка клика не требуется, т.к. кнопка открывает Web App
    await query.answer()  # Просто подтверждаем получение запроса


async def main():
    # Запуск бота
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
