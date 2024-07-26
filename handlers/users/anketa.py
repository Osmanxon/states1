from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PersonalData

@dp.message_handler(Command("from"),state=None)
async def enter_test(message: types.Message):
    await message.answer("Toliq ismigizni kiriting")
    await PersonalData.fullName.set()

@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname=message.text

    await state.update_data(
        {"name": fullname}
    )

    await message.answer("Email manzil kiriting")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email=message.text

    await state.update_data(
        {"email": email}
    )

    await message.answer("Telefon raqam kiriting")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):
    phone=message.text

    await state.update_data(
        {"phone": phone}
    )

    #Malumotlarni qayta o'qiymiz
    data = await state.update_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    msg = "Quyidagi malumotlar qabul qilindi:\n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Email - {email}\n"
    msg += f"Telefon:-{phone}"
    await message.answer(msg)

    # State dan chiqaramiz
    await state.finish()


































