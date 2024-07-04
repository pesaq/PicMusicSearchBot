from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from core.settings import settings
from core.keyboards.help_keyboard import help_board

basicrouter = Router()

@basicrouter.startup()
async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot started')
@basicrouter.shutdown()
async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot stoped')

@basicrouter.message(Command(commands=['start']))
async def get_start(message: Message):
    await message.answer('Привет! Я бот для поиска музыки', reply_markup=help_board)

@basicrouter.callback_query(F.data == 'help_callback')
async def get_help(callback: CallbackQuery):
    await callback.message.answer('''Список команд бота:
/start - начало работы

/search (текст) - поиск трека по названию/автору
/setcount (число) - установить количество треков для поиска (списком)''')