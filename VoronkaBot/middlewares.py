from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable
from localization import translations


class TranslationMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        text = data["text"]
        ru_texts = translations["en"].keys()
        if text in ru_texts:
            return await handler(event, data)
        else:
            data["text"] = [list(translations["en"].values()).index(text)]
            return await handler(event, data)
