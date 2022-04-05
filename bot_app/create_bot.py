from . import local_settings
from aiogram import Bot, Dispatcher




bot = Bot(token=local_settings.API_KEY)
dp = Dispatcher(bot)