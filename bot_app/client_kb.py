from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from . import commands
from . import create_bot


b11 = KeyboardButton("/Start")
b12 = KeyboardButton("/Помощь")
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client_in = InlineKeyboardMarkup()

b21 = InlineKeyboardButton(text= "На_сайт", url="https://molotovfit.ru/")
b22 = InlineKeyboardButton(text= "facebook", url="https://www.facebook.com/profile.php?id=100003740662311")
b23 = InlineKeyboardButton(text= "Телефон", callback_data="button_tel")
#callback_data='button_tel'
b24 = InlineKeyboardButton(text= "whatsapp", url="whatsapp://send?phone=+79858222637")
b25 = InlineKeyboardButton(text= "Страница_в_VK", url="https://vk.com/danny.molotov")
b26 = InlineKeyboardButton(text= "Почта", url="whatsapp://send?phone=+79858222637")
b27 = InlineKeyboardButton(text= "instagram", url="https://www.instagram.com/dannymolotov/")

#b30 = InlineKeyboardButton(text= f"Привет {commands.messege.from_user.first_name} "
    #                             f"если интересно то ваш ID: {commands.messege.from_user.id},  ")

kb_client.row(b11,b12)#.row(b13,b15)#add(b1).insert(b2).insert(b3).add(b4)
#kb_client_in.row(b21,b25).row(b22,b27).row(b23,b24).row(b26,b26)
kb_client_in.row(b21,b25).row(b22,b27)
#kb_client_in.row(b21,b21).row(b21,b21)
#kb_client_in.add(b21, b22, b25, b27)
