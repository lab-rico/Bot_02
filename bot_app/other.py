import asyncio
import aioschedule
from aiogram import bot, types, Dispatcher
from . import messeges
from . import create_bot
from . import client_kb
from aiogram.utils import executor


async def noon_print():
    print("It's noon!")

async def scheduler():
    print("It's noon!")

async def send_help02(messege: types.Message):
    await messege.reply(messeges.WELCOME_MESSAGE)

async def scheduler2():
    #aioschedule.every().day.at("17:45").do(noon_print)
    #aioschedule.schedule.every(3).seconds.do(send_help02)
    aioschedule.every(1).seconds.do(noon_print)
    while True:
         await aioschedule.run_pending()
         await asyncio.sleep(1)

async def on_startup(dp):
    #asyncio.create_task(scheduler())
    print("on_startup терминал")

#def register_handlers_client(dp: Dispatcher):
 #   dp.register_message_handler(send_help02, commands=["ti"])

#if __name__ == '__other__':
 #       executor.start_polling(on_startup=on_startup)