from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from states.personalData import PersonalData


@dp.message_handler(CommandHelp(), state=PersonalData.fullName)
async def bot_help(message: types.Message):
    text = ("Siz bu joyda ism \n familiyangizni kiritishingiz kerak")
    
    await message.answer("\n".join(text))


@dp.message_handler(CommandHelp(),)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))