from aiogram import bot, types, Dispatcher
from . import messeges
from . import create_bot
from . import client_kb



#@dp.message_handler(commands=["start", "help"])
async def send_welcom(messege: types.Message):
    await messege.reply(messeges.WELCOME_MESSAGE, reply_markup= client_kb.kb_client)

async def send_help(message: types.Message):
    await message.answer(messeges.WELCOME_HELP, reply_markup=client_kb.kb_client_in)

#@dp.message_handler(commands=["Ваше имя и id"])
async def send_welcom_id(messege: types.Message):
    #await messege.answer(f"Ваш ID: {messege.from_user.id}, {messege.from_user.first_name}, {messege.from_user.last_name}, {messege.from_user.username}")
    await messege.answer(f"Привет {messege.from_user.first_name} если интересно то ваш ID: {messege.from_user.id},  ")

#@dp.message_handler(commands=["tg"])
async def send_welcom_tel(messege: types.Message):
    await messege.reply("Телефон: \n\n +79858223637")

async def send_welcom_vk(messege: types.Message):
    await messege.reply("Страница в VK: \n https://vk.com/danny.molotov")

async def send_welcom_mail(messege: types.Message):
    await messege.reply("Почта: \n molotov@motogon.ru")
    print("Почта терминал")

from .create_bot import bot


async def send_ti(message: types.Message):
    #await message.answer("Время: \n ")
    await bot.send_message(message.from_user.id, "Время")
    print("Время терминал")



import asyncio
import aioschedule



async def scheduler():
    aioschedule.every(2).seconds.do(send_ti)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(dp):
    asyncio.create_task(scheduler())

#async def send_welcom_tel2(callback_query: types.CallbackQuery):
 #   await bot.answer_callback_query(callback_query.id)
  #  await bot.send_message(callback_query.from_user.id, '*+79858223637*', parse_mode="Markdown")

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(on_startup, commands=["ti"])
    dp.register_message_handler(send_welcom, commands=["Start"])
    dp.register_message_handler(send_help, commands=["Помощь", "help"])
    dp.register_message_handler(send_welcom_id, commands=["Ваше_имя_и_id", "id"])
    dp.register_message_handler(send_welcom_vk, commands=["Страница_в_VK", "VK"])
    dp.register_message_handler(send_welcom_mail, commands=["Почта", "EMail"])
    #dp.register_message_handler(send_welcom_tel2, commands=["Телефон", "Telefon"])
    dp.register_message_handler(send_welcom_tel, commands=["Телефон", "Telefon"])

