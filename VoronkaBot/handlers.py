from pathlib import Path
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from states import *
from aiogram.dispatcher import FSMContext
from load_config import *
from menus import *
from states import MenuStates
from aiogram.dispatcher.filters import MediaGroupFilter
from typing import List
from pathlib import Path
import asyncio
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from load_config import BOT_KEY, DB_PATH
from db_class import db
from localization import local, ghl
from middlewares import TranslationMiddleware

bot = Bot(token=BOT_KEY, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(TranslationMiddleware())


@ dp.message_handler(commands="start")
async def greet(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id, "ru")
        await message.answer("Language\nЯзык", reply_markup=language_menu)
    else:
        await message.answer("Language\nЯзык", reply_markup=language_menu)


@dp.callback_query_handler(lambda cb: cb.data in ["ru", "en"])
async def _(query: types.CallbackQuery):
    db.set_lang(query.from_user.id, query.data)
    await query.message.answer(local("Язык выбран!", query.from_user.id))
    await query.message.answer(local("Привет это бот воронки!", query.from_user.id), reply_markup=main_menu(db.get_lang(query.from_user.id)))


@ dp.message_handler(Text(equals="Стать партнером"))
async def _(message: types.Message):
    await message.answer(local("Если вы хотите стать партнером Воронки, можете связаться с CEO: @shvetsov_07, который с радостью ответит на все интересующие вопросы", message.from_user.id))


@dp.message_handler(Text(equals="Как я могу помочь с развитием приложения?"))
async def _(message: types.Message):
    await message.answer(local("Выберите вариант из меню", message.from_user.id), reply_markup=support_menu(db.get_lang(message.from_user.id)))
    await MenuStates.support_project.set()


@dp.message_handler(Text(equals="Хочу пополнить баланс копилки на кофе или комплекс команде!"), state=MenuStates.support_project)
async def _(message: types.Message):
    await message.answer(local("Вау! Мы очень рады, спасибо тебе большое)) Вот ссылка на нашу копилку", message.from_user.id), reply_markup=kopilka_menu)


@dp.message_handler(Text(equals="Хочу рассказать о вас друзьям!"), state=MenuStates.support_project)
async def _(message: types.Message):
    await message.answer(local("""Это лучшая помощь для нас, спасибо тебе!
Вот небольшое сообщение, которое ты можешь переслать своим друзьям:
привет, хочу поделиться с тобой сервисом о студлайфе вышки! Ребята сделали приложение, которое помогает найти ивент по твоим интересам и зарегистрироваться на него.
Подписывайся на их телеграм-канал, скачивай приложение в AppStore или PlayMarket, а еще забирай крутой стикерпак!
""", message.from_user.id))


@dp.message_handler(Text(equals="Change language"))
async def _(message: types.Message):
    await message.answer("Language\nЯзык", reply_markup=language_menu)

# Back buttons


@dp.message_handler(Text(equals="Назад"), state=MenuStates.support_project)
async def _(message: types.Message):
    await message.answer(local("Главное меню", message.from_user.id), reply_markup=main_menu(db.get_lang(message.from_user.id)))


def start_bot(dp: Dispatcher):
    executor.start_polling(dp, skip_updates=True)
