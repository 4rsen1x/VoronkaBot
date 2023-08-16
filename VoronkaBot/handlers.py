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
from advanced_localization import local
from middlewares import TranslationMiddleware
from aiogram.types import InputFile
from aiogram_media_group import media_group_handler
import logging

bot = Bot(token=BOT_KEY, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(TranslationMiddleware())


@ dp.message_handler(commands="start")
async def greet(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id, "ru")
        await message.answer(local("start_pick_lang", message.from_id), reply_markup=language_menu)
    else:
        await message.answer(local("start_pick_lang", message.from_id), reply_markup=language_menu)

# Back buttons


@dp.message_handler(Text(equals="Назад"), state=ErrorStates.platform)
async def _(message: types.Message, state: FSMContext):
    await state.finish()
    await main_view(message)


@dp.message_handler(Text(equals="Назад"), state=ErrorStates.report)
async def _(message: types.Message, state: FSMContext):
    await state.finish()
    await main_view(message)


@dp.message_handler(Text(equals="Назад"), state=MenuStates.support_project)
async def _(message: types.Message):
    # await message.answer(local("Главное меню", message.from_user.id), reply_markup=main_menu(message.from_user.id))
    await main_view(message)


@dp.message_handler(Text(equals="Назад"), state=MenuStates.our_mission)
async def _(message: types.Message):
    await about_voronka(message)


@dp.message_handler(Text(equals="Назад"), state=MenuStates.download_app)
async def _(message: types.Message):
    await about_service(message)


@dp.message_handler(Text(equals="Назад"), state=MenuStates.about_service)
async def _(message: types.Message):
    await about_voronka(message)


@dp.message_handler(Text(equals="Назад"), state=MenuStates.about_features)
async def _(message: types.Message):
    await about_service(message)


@dp.message_handler(Text(equals="Назад"), state=MenuStates.about_team)
async def _(message: types.Message):
    await about_voronka(message)


@dp.message_handler(Text(equals="Назад"), state=MenuStates.about_voronka)
async def _(message: types.Message):
    await main_view(message)


@dp.message_handler(Text(equals="Назад"), state=NewFeatureStates.new_feature)
async def _(message: types.Message, state: FSMContext):
    await state.finish()
    await about_service(message)


@dp.message_handler(Text(equals="Назад"), state=MenuStates.new_feature)
async def _(message: types.Message):
    await about_service(message)


@dp.message_handler(Text(equals="Назад"), state=MenuStates.change_stud_life)
async def _(message: types.Message):
    await about_voronka(message)


@dp.message_handler(Text(equals="Назад"), state=MenuStates.change_studlife_from_support)
async def _(message: types.Message):
    await help_with_promotion(message)


@dp.message_handler(Text(equals="Назад"), state=MenuStates.change_studlife_from_our_mission)
async def _(message: types.Message):
    await our_mission(message)


@dp.message_handler(Text(equals="Назад"), state=MenuStates.change_studlife_from_team)
async def _(message: types.Message):
    await about_team(message)


@dp.message_handler(Text(equals="Назад"), state=GetCVStates.cv)
async def _(message: types.Message):
    await change_studlife(message)


@dp.message_handler(Text(equals="Назад"), state="*")
async def main_view(message: types.Message):
    await message.answer(local("greet", message.from_user.id), reply_markup=main_menu(message.from_user.id))


@dp.message_handler(Text(equals="В начало"), state="*")
async def _(message: types.Message, state: FSMContext):
    await state.finish()
    # await message.answer(local("Привет это бот воронки!", message.from_user.id), reply_markup=main_menu(message.from_user.id))
    await main_view(message)


@dp.callback_query_handler(lambda cb: cb.data in ["ru", "en"], state="*")
async def language_set(query: types.CallbackQuery):
    db.set_lang(query.from_user.id, query.data)
    await query.message.answer(local("language_set", query.from_user.id))
    await query.message.answer(local("greet", query.from_user.id), reply_markup=main_menu(query.from_user.id))


@ dp.message_handler(Text(equals="Стать партнером"), state="*")
async def become_partner(message: types.Message):
    await message.answer(local("become_partner", message.from_user.id))


@dp.message_handler(Text(equals="Как я могу помочь с развитием приложения?"), state="*")
async def help_with_promotion(message: types.Message):
    await message.answer(local("help_with_promotion", message.from_user.id), reply_markup=support_menu(message.from_user.id))
    await MenuStates.support_project.set()


@dp.message_handler(Text(equals="Хочу пополнить баланс копилки на кофе или комплекс команде!"), state="*")
async def leave_tip(message: types.Message):
    await message.answer(local("leave_tip", message.from_user.id), reply_markup=kopilka_menu(message.from_user.id))


@dp.message_handler(Text(equals="Хочу рассказать о вас друзьям!"), state="*")
async def tell_friends(message: types.Message):
    await message.answer(local("tell_friends", message.from_user.id))


@dp.message_handler(Text(equals="Change language"), state="*")
async def change_language(message: types.Message):
    await message.answer(local("start_message", message.from_id), reply_markup=language_menu)


@dp.message_handler(Text(equals="О воронке"), state="*")
async def about_voronka(message: types.Message):
    await MenuStates.about_voronka.set()
    await message.answer(local("about_voronka", message.from_id), reply_markup=about_voronka_menu(message.from_user.id))


@dp.message_handler(Text(equals="Наша миссия"), state="*")
async def our_mission(message: types.Message):
    # await message.answer(
    #     local("our_mission", message.from_id),
    #     reply_markup=change_studlife_menu(message.from_user.id)
    # )
    await message.answer_photo(
        InputFile("media/our_mission.jpg"),
        caption=local("our_mission", message.from_id),
        reply_markup=change_studlife_menu(message.from_user.id)
    )
    await MenuStates.our_mission.set()


@dp.message_handler(Text(equals="О сервисе"), state="*")
async def about_service(message: types.Message):
    # await message.answer(
    #     local(
    #         "about_service", message.from_id
    #     ),
    #     reply_markup=about_service_menu(message.from_user.id)
    # )
    await message.answer_photo(
        InputFile("media/about_service.jpg"),
        caption=local(
            "about_service", message.from_id
        ),
        reply_markup=about_service_menu(message.from_user.id)
    )
    await MenuStates.about_service.set()


@dp.message_handler(Text(equals="О команде"), state="*")
async def about_team(message: types.Message):
    # await message.answer(
    #     local(
    #         "about_team", message.from_id
    #     ),
    #     reply_markup=change_studlife_menu(message.from_user.id)
    # )
    await message.answer_photo(
        InputFile("media/about_team.jpg"),
        caption=local(
            "about_team", message.from_id
        ),
        reply_markup=change_studlife_menu(message.from_user.id)
    )
    await MenuStates.about_team.set()


@dp.message_handler(Text(equals="Подробнее о фичах"), state="*")
async def about_features(message: types.Message):
    await message.answer(
        local("about_features", message.from_id),
        reply_markup=about_features_menu(message.from_id)
    )
    await MenuStates.about_features.set()


@dp.message_handler(Text(equals="Выбор интересов"), state="*")
async def pick_interests(message: types.Message):
    # await message.answer(
    #     local("pick_interests", message.from_id)
    # )
    await message.answer_animation(
        InputFile("media/pick_interests.gif"),
        caption=local("pick_interests", message.from_id)
    )


@dp.message_handler(Text(equals="Интеграция с ЕЛК"), state="*")
async def integrate_with_elk(message: types.Message):
    # await message.answer(
    #     local("integrate_with_elk", message.from_id)
    # )
    await message.answer_animation(
        InputFile("media/elk_integration.gif"),
        caption=local("integrate_with_elk", message.from_id)
    )


@dp.message_handler(Text(equals="Лента мероприятий"), state="*")
async def event_feed(message: types.Message):
    # await message.answer(
    #     local("event_feed", message.from_id)
    # )
    await message.answer_animation(
        InputFile("media/event_feed.gif"),
        caption=local("event_feed", message.from_id)
    )


@dp.message_handler(Text(equals="Мои ивенты"), state="*")
async def my_events(message: types.Message):
    # await message.answer(
    #     local("my_events", message.from_id)
    # )
    await message.answer_animation(
        InputFile("media/my_events.gif"),
        caption=local("my_events", message.from_id)
    )


@dp.message_handler(Text(equals="Профиль студенческой организации"), state="*")
async def organisation_profile(message: types.Message):
    # await message.answer(
    #     local("organisation_profile", message.from_id)
    # )
    await message.answer_animation(
        InputFile("media/organisation_profile.gif"),
        caption=local("organisation_profile", message.from_id)
    )


@dp.message_handler(Text(equals="У меня есть идея для новой фичи!"), state="*")
async def new_feature_idea(message: types.Message):
    await message.answer(
        local("new_feature_idea", message.from_id),
        reply_markup=back_begin_menu(message.from_id)
    )
    await NewFeatureStates.new_feature.set()


@dp.message_handler(state=NewFeatureStates.new_feature, content_types=types.ContentType.ANY)
async def new_feature_sent_single_media(message: types.Message, state: FSMContext):
    try:
        await bot.send_message(
            GROUP_ID,
            f"Новая фича от {message.from_user.get_mention()}"
        )
        await message.forward(GROUP_ID)
    except Exception as e:
        logging.error(str(e))
    await state.finish()
    await message.answer(
        local(
            "new_feature_sent",
            message.from_id
        )
        # reply_markup=back_begin_menu(message.from_id)
    )
    await MenuStates.new_feature.set()
    await main_view(message)


@dp.message_handler(state=NewFeatureStates.new_feature, is_media_group=True, content_types=types.ContentType.ANY)
@media_group_handler
async def new_feature_sent_media_group(messages: List[types.Message], state: FSMContext):
    try:
        await bot.send_message(
            GROUP_ID,
            f"Новая фича от {messages[0].from_user.get_mention()}"
        )
        for message in messages:
            await message.forward(GROUP_ID)
    except Exception as e:
        logging.error(str(e))
    await state.finish()
    await messages[0].answer(
        local(
            "new_feature_sent",
            message.from_id
        )
        # reply_markup=back_begin_menu(message.from_id)
    )
    await MenuStates.new_feature.set()
    await main_view(messages[0])


@dp.message_handler(Text(equals="Скачать приложение"), state="*")
async def download_app(message: types.Message):
    await message.answer(
        local("download_app", message.from_id),
        reply_markup=device_menu(message.from_id)
    )
    await MenuStates.download_app.set()


@dp.message_handler(Text(equals="У меня Android!"), state="*")
async def i_have_android(message: types.Message):
    await message.answer(
        local("i_have_android", message.from_id),
        reply_markup=inline_download_android(message.from_id)
    )


@dp.message_handler(Text(equals="У меня IOS!"), state="*")
async def i_have_iphone(message: types.Message):
    await message.answer(
        local("i_have_iphone", message.from_id),
        reply_markup=inline_download_ios(message.from_id)
    )


@dp.message_handler(Text(equals="Хочу подписаться на телеграм-канал!"), state="*")
async def follow_tg_channel(message: types.Message):
    await message.answer(
        local(
            "follow_tg_channel",
            message.from_id
        ),
        reply_markup=inline_tg_channel(message.from_id)
    )


@dp.message_handler(Text(equals="Хочу ваши стикеры!"), state="*")
async def get_stickers(message: types.Message):
    await message.answer(
        local(
            "get_stickers",
            message.from_id
        )
    )
    await message.answer_sticker(
        sticker=STICKER_ID
    )


@dp.message_handler(Text(equals="А можно глянуть лендинг?"), state="*")
async def show_landing(message: types.Message):
    await message.answer(
        local(
            "show_landing",
            message.from_id
        ),
        reply_markup=inline_landing_link(message.from_id)
    )


@dp.message_handler(Text(equals="Сообщить об ошибке"), state="*")
async def report_issue(message: types.Message):
    await message.answer(
        local(
            "report_issue",
            message.from_id
        ),
        reply_markup=error_report_menu(message.from_id)
    )
    await ErrorStates.platform.set()


@dp.message_handler(
    lambda msg: msg.text in [
        "Лендинг", "Я организатор", "Бот", "Приложение на Android", "Приложение на iOS"],
    state=ErrorStates.platform
)
async def get_platform(message: types.Message, state: FSMContext):
    await state.update_data(platform=message.text)
    await message.answer(
        local(
            "get_platform",
            message.from_id
        ),
        reply_markup=back_begin_menu(message.from_id)
    )
    await ErrorStates.report.set()


@dp.message_handler(state=ErrorStates.report, is_media_group=True, content_types=types.ContentType.ANY)
@media_group_handler
async def error_report_sent_media_group(messages: List[types.Message], state: FSMContext):
    data = await state.get_data()
    platform = data.get("platform")
    try:
        await bot.send_message(
            GROUP_ID,
            f"Сообщение об ошибке от {messages[0].from_user.get_mention()}\nПлатформа: {platform}"
        )
        for message in messages:
            await message.forward(GROUP_ID)
    except Exception as e:
        logging.error(str(e))
    await state.finish()
    await message.answer(
        local(
            "error_report_sent",
            message.from_id
        )
        # reply_markup=main_menu(message.from_id)
    )
    await main_view(messages[0])


@dp.message_handler(state=ErrorStates.report, content_types=types.ContentType.ANY)
async def error_report_sent_single_media(message: types.Message, state: FSMContext):
    data = await state.get_data()
    platform = data.get("platform")
    try:
        await bot.send_message(
            GROUP_ID,
            f"Сообщение об ошибке от {message.from_user.get_mention()}\nПлатформа: {platform}"
        )
        await message.forward(GROUP_ID)
    except Exception as e:
        logging.error(str(e))
    await state.finish()
    await message.answer(
        local(
            "error_report_sent",
            message.from_id
        )
        # reply_markup=main_menu(message.from_id)
    )
    await main_view(message)


@dp.message_handler(Text(equals="Хочу менять студлайф с вами!"), state=MenuStates.about_team)
async def change_studlife(message: types.Message):
    await message.answer(
        local(
            "change_studlife",
            message.from_id
        ),
        reply_markup=studlife_menu(message.from_id)
    )
    await MenuStates.change_studlife_from_team.set()


@dp.message_handler(Text(equals="Хочу менять студлайф с вами!"), state=MenuStates.our_mission)
async def change_studlife(message: types.Message):
    await message.answer(
        local(
            "change_studlife",
            message.from_id
        ),
        reply_markup=studlife_menu(message.from_id)
    )
    await MenuStates.change_studlife_from_our_mission.set()


@dp.message_handler(Text(equals="Хочу менять студлайф с вами!"), state=MenuStates.support_project)
async def change_studlife(message: types.Message):
    await message.answer(
        local(
            "change_studlife",
            message.from_id
        ),
        reply_markup=studlife_menu(message.from_id)
    )
    await MenuStates.change_studlife_from_support.set()


@dp.message_handler(Text(equals="Хочу менять студлайф с вами!"), state=MenuStates.about_voronka)
async def change_studlife(message: types.Message):
    await message.answer(
        local(
            "change_studlife",
            message.from_id
        ),
        reply_markup=studlife_menu(message.from_id)
    )
    await MenuStates.change_stud_life.set()


@dp.message_handler(Text(equals="Посмотреть доступные вакансии"), state="*")
async def get_cv_single_media(message: types.Message):
    await message.answer(
        local(
            "get_cv",
            message.from_id
        ),
        reply_markup=back_begin_menu(message.from_id)
    )
    await GetCVStates.cv.set()


@dp.message_handler(state=GetCVStates.cv, is_media_group=True, content_types=types.ContentType.ANY)
@media_group_handler
async def cv_sent_media_group(messages: List[types.Message], state: FSMContext):
    try:
        await bot.send_message(
            GROUP_ID,
            f"CV от {messages[0].from_user.get_mention()}"
        )
        for message in messages:
            await message.forward(GROUP_ID)
    except Exception as e:
        logging.error(str(e))
    await messages[0].answer(
        local(
            "cv_sent",
            message.from_id
        )
        # reply_markup=back_begin_menu(messages[0].from_id)
    )
    await state.finish()
    await main_view(messages[0])


@dp.message_handler(state=GetCVStates.cv, content_types=types.ContentType.ANY)
async def cv_sent(message: types.Message, state: FSMContext):
    try:
        await bot.send_message(
            GROUP_ID,
            f"CV от {message.from_user.get_mention()}"
        )
        await message.forward(GROUP_ID)
    except Exception as e:
        logging.error(str(e))
    await message.answer(
        local(
            "cv_sent",
            message.from_id
        )
        # reply_markup=back_begin_menu(message.from_id)
    )
    await state.finish()
    await main_view(message)


def start_bot(dp: Dispatcher):
    executor.start_polling(dp, skip_updates=True)
