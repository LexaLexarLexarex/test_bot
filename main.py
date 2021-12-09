from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import keyboards as kb
from aiogram.dispatcher.filters import Text
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Добро пожаловать в телеграмм бота для юристов!\nВыберите пункт меню", reply_markup=kb.start_kb)


@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.answer("ОЧЕНЬ ОЧЕНЬ ПОМОГАЕМ")


@dp.message_handler(Text(equals="🤟Профиль"))
async def process_by_profile(message:types.Message):
    await message.answer(f"Название компании: {message.from_user.first_name}\nРеквизиты:{message.from_user.id}", reply_markup= kb.profile_kb)


@dp.message_handler(Text(equals="📃Документ"))
async def process_by_document(message: types.Message):
    await message.answer("Выберите документ:", reply_markup=kb.doc_kb)


@dp.message_handler(Text(equals="🔍Искать статью"))
async def process_by_topic(message: types.Message):
    await message.answer("Старательно ищем", reply_markup=kb.profile_kb)


@dp.message_handler(Text(equals="☺Поддержка"))
async def process_by_support(message: types.Message):
    await message.answer("Старательно поддерживаем", reply_markup=kb.profile_kb)


@dp.callback_query_handler(lambda c: c.data == 'off')
async def process_by_offers(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Выберите Договор", reply_markup=kb.contract_kb)


@dp.callback_query_handler(lambda c: c.data == 'rent')
async def process_by_rent(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Выберите Договор", reply_markup=kb.choose_doc)


@dp.callback_query_handler(lambda c: c.data == 'back1')
async def process_by_rent(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Выберите документ:", reply_markup=kb.doc_kb)


@dp.callback_query_handler(lambda c: c.data == 'menu')
async def process_by_menu(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Добро пожаловать в телеграмм бота для юристов!\nВыберите пункт меню", reply_markup=kb.start_kb)


if __name__ == '__main__':
    executor.start_polling(dp)
