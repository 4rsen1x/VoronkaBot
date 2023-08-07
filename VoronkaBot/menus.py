from aiogram import types
from localization import local


def main_menu(lang):
    main_kb = [
        [types.KeyboardButton(text=local("О воронке", lang))],
        [types.KeyboardButton(text=local("Сообщить об ошибке", lang))],
        [types.KeyboardButton(
            text=local("Как я могу помочь с развитием приложения?", lang))],
        [types.KeyboardButton(text=local("Стать партнером", lang))],
        [types.KeyboardButton(text="Change language")]
    ]
    menu = types.ReplyKeyboardMarkup(keyboard=main_kb, resize_keyboard=True)
    return menu


def support_menu(lang):
    support_kb = [
        [types.KeyboardButton(text=local(
            "Хочу менять студлайф с вами!", lang))],
        [types.KeyboardButton(
            text=local("Хочу пополнить баланс копилки на кофе или комплекс команде!", lang))],
        [types.KeyboardButton(text=local(
            "Хочу рассказать о вас друзьям!", lang))],
        [types.KeyboardButton(text=local("Стать партнером", lang))],
        [types.KeyboardButton(text=local("Назад", lang))],
    ]
    menu = types.ReplyKeyboardMarkup(
        keyboard=support_kb, resize_keyboard=True)
    return menu


def kopilka_menu(lang):
    menu = types.InlineKeyboardMarkup()
    kopilka_button = types.InlineKeyboardButton("наша копилка", url="ya.ru")
    menu.add(kopilka_button)


language_menu = types.InlineKeyboardMarkup()
language_button_ru = types.InlineKeyboardButton(
    text="Русский", callback_data="ru")
language_button_en = types.InlineKeyboardButton(
    text="English", callback_data="en")
language_menu.add(language_button_ru)
language_menu.add(language_button_en)
