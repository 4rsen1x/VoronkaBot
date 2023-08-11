from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable
from advanced_localization import translations
from aiogram import types
from db_class import db


class TranslationMiddleware(BaseMiddleware):
    def __init__(self):
        super(TranslationMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, *args):
        ru_texts = translations["ru"].values()
        if message.text in ru_texts:
            return
        else:
            try:
                lang = db.get_lang(message.from_id)
                message_name = list(translations.keys())[list(
                    translations.values()).index(message.text)]
                message.text = translations["ru"][message_name]
                return
            except Exception as e:
                return
