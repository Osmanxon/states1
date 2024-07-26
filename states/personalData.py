from aiogram.dispatcher.filters.state import StatesGroup, State

#Shaxsiy malumotlarni yigish uchun PersonalData holatdan yaratamiz

class PersonalData(StatesGroup):
    fullName=State()
    email=State()
    phoneNum=State()