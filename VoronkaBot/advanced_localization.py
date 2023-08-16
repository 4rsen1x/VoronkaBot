import logging
from db_class import db
translations = {
    "ru": {
        "start_message": "Language\nЯзык",
        "language_set": "Язык выбран!",
        "greet": "Привет это бот воронки!",
        "become_partner": "Если вы хотите стать партнером Воронки, можете связаться с CEO: @shvetsov_07, который с радостью ответит на все интересующие вопросы",
        "help_with_promotion": "Выберите вариант из меню",
        "leave_tip": "Вау! Мы очень рады, спасибо тебе большое)) Вот ссылка на нашу копилку",
        "tell_friends": """Это лучшая помощь для нас, спасибо тебе!
Вот небольшое сообщение, которое ты можешь переслать своим друзьям:
привет, хочу поделиться с тобой сервисом о студлайфе вышки! Ребята сделали приложение, которое помогает найти ивент по твоим интересам и зарегистрироваться на него.
Подписывайся на их телеграм-канал, скачивай приложение в AppStore или PlayMarket, а еще забирай крутой стикерпак!
""",
        "change_language": "",
        "about_voronka": "Что такое воронка?",
        "our_mission": """Фото человечка из брендбука + текст:
Все просто: мы хотим объединить всех студентов вышки и сделать студлайф ярким, насыщенным, ярким и доступным.""",
        "about_service": """Что такое Воронка?
Воронка — это мобильное приложение для студентов, желающих разнообразить внеучебную жизнь.
Это персонализированные подборки мероприятий по твоим интересам в формате рилсов, регистрация на них в пару кликов, интеграция с ЕЛК, все о каждой студенческой организации и многое другое!
Воронка обещает сделать твой студлайф незабываемым!""",
        "about_team": "Выше на фото вы можете видеть нашу команду. Нас 9 и я хз что еще написать)",
        "about_features": "О какой фиче ты хочешь узнать более подробно?",
        "pick_interests": """Видео/гифка + текст:
В Вышке постоянно проходит множество ивентов, а каждый ивент - это уникальное событие, которое отвечает разным интересам. Поиск мероприятий станет еще удобнее с системой тегов. Она позволит делать более точные рекомендации, а визуальное выделение в ленте подскажет, чем каждое мероприятие может заинтересовать именно тебя. Ты можешь выбрать от 5 до 20 тегов, в зависимости от которых будут формироваться рекомендации в основной ленте.
Теперь поиск ивента благодаря выбору интересов придется по душе!""",
        "integrate_with_elk": """Видео/гифка + текст:
Новый сервис - это очередная регистрация, очередные поля для ввода информации о себе... Но!
Мы постарались и максимально упростили этот муторный процессс: Воронка интегрируется с ЕЛК НИУ ВШЭ, что позволяет пройти регистрацию или войти в приложение всего в пару кликов!""",
        "event_feed": """Видео/гифка + текст:
Лента мероприятий - сердце нашего сервиса. Теперь все анонсы в одном месте! Они персонализированы и соответствуют твоим интересам. А еще это привычный формат, который сделан в виде рилсов! Теперь дело за тобой: листай, находи, регистрируйся и иди!""",
        "my_events": """Видео/гифка + текст:
Тебе понравилось мероприятие, но пока не уверен, что сможешь пойти на него? Или ты уже зарегистрировался и хочешь посмотреть, когда и где оно состоится? Эта фича решает твою проблему: управляй своими ивентами быстро и в пару кликов!""",
        "organisation_profile": """Видео/гифка + текст:
Посмотри информацию об интересующей тебя студенческой организации и ее анонсах""",
        "new_feature_idea": "Нам очень приятно, что ты хочешь поделиться своей идеей с нами! Опиши ее и скажи, какую проблему она решит",
        "new_feature_sent": "Спасибо большое за то, что поделился / поделилась своей идей! Мы обязательно дадим обратную связь в ближайшее время)",
        "download_app": "Какое у вас устройство?",
        "i_have_android": "Лови ссылку на скачивание приложения в PlayMarket и скорее начинай пользоваться всеми возможностями Воронки, чтобы с головой окунуться в насыщенный и яркий студлайф!",
        "i_have_iphone": "Лови ссылку на скачивание приложения в AppStore и скорее начинай пользоваться всеми возможностями Воронки, чтобы с головой окунуться в насыщенный и яркий студлайф!",
        "follow_tg_channel": "Лови ссылку на телеграм-канал Воронки, подписывайся, следи за апдейтами и не упускай новости и релизы новых фич!",
        "get_stickers": "Забирай наш стикерпак и делись стикерами с друзьями)",
        "show_landing": """Да, конечно!
Держи ссылку на него""",
        "report_issue": "И как это мы так все тестили... Давай разбираться, где была найдена ошибка!",
        "get_platform": "Пожалуйста, прикрепи фото/видео возникшей проблемы и опиши её",
        "error_report_sent": "Большое спасибо за сообщение об ошибке! Мы постараемся обязательно исправить ее в ближайшее время",
        "about_voronka_button": "О воронке",
        "report_problem_button": "Сообщить об ошибке",
        "help_with_promotion_button": "Как я могу помочь с развитием приложения?",
        "become_partner_button": "Стать партнером",
        "change_language_button": "Change language",
        "change_studlife_button": "Хочу менять студлайф с вами!",
        "leave_tip_button": "Хочу пополнить баланс копилки на кофе или комплекс команде!",
        "tell_friends_button": "Хочу рассказать о вас друзьям!",
        "back_button": "Назад",
        "our_kopilka_button": "наша копилка",
        "ru_lang_button": "Русский",
        "en_lang_button": "English",
        "about_team_button": "О команде",
        "about_service_button": "О сервисе",
        "our_mission_button": "Наша миссия",
        "to_begin_button": "В начало",
        "about_features_button": "Подробнее о фичах",
        "new_feature_button": "У меня есть идея для новой фичи!",
        "download_app_button": "Скачать приложение",
        "follow_tg_channel_button": "Хочу подписаться на телеграм-канал!",
        "get_stickers_button": "Хочу ваши стикеры!",
        "show_landing_button": "А можно глянуть лендинг?",
        "pick_interests_button": "Выбор интересов",
        "integrate_elk_button": "Интеграция с ЕЛК",
        "event_feed_button": "Лента мероприятий",
        "my_events_button": "Мои ивенты",
        "organisation_profile_button": "Профиль студенческой организации",
        "new_feature_idea_button": "У меня есть идея для новой фичи!",
        "i_have_android_button": "У меня Android!",
        "i_have_ios_button": "У меня IOS!",
        "download_button": "скачать",
        "follow_button": "подписаться",
        "open_button": "перейти",
        "landing_button": "Лендинг",
        "ios_app_button": "Приложение на iOS",
        "android_app_button": "Приложение на Android",
        "bot_app_button": "Бот",
        "i_am_organisation_button": "Я организатор",
        "show_vacancies_button": "Посмотреть доступные вакансии",
        "change_studlife": "Выберите из меню: ",
        "get_cv": "Если ты очень хочешь стать частью нашей команды, расскажи, каким образом ты можешь быть нам помочь и по возможности прикрепи CV",
        "cv_sent": "Спасибо! Мы обязательно напишем тебе в ближайшее время!",
        "start_pick_lang": "Language\nЯзык",
    },
    "en": {
        "start_message": "Language\nЯзык",
        "language_set": "",
        "greet": "",
        "become_partner": "",
        "help_with_promotion": "",
        "leave_tip": "",
        "tell_friends": "",
        "change_language": "",
        "about_voronka": "",
        "our_mission": "",
        "about_service": "",
        "about_team": "",
        "about_features": "",
        "pick_interests": "",
        "integrate_with_elk": "",
        "event_feed": "",
        "my_events": "",
        "organisation_profile": "",
        "new_feature_idea": "",
        "new_feature_sent": "",
        "download_app": "",
        "i_have_android": "",
        "i_have_iphone": "",
        "follow_tg_channel": "",
        "get_stickers": "",
        "show_landing": "",
        "report_issue": "",
        "get_platform": "",
        "error_report_sent": "",
        "about_voronka_button": "",
        "report_problem_button": "",
        "help_with_promotion_button": "",
        "become_partner_button": "",
        "change_language_button": "",
        "change_studlife_button": "",
        "leave_tip_button": "",
        "tell_friends_button": "",
        "back_button": "",
        "our_kopilka_button": "",
        "ru_lang_button": "",
        "en_lang_button": "",
        "about_team_button": "",
        "about_service_button": "",
        "our_mission_button": "",
        "to_begin_button": "",
        "about_features_button": "",
        "new_feature_button": "",
        "download_app_button": "",
        "follow_tg_channel_button": "",
        "get_stickers_button": "",
        "show_landing_button": "",
        "pick_interests_button": "",
        "integrate_elk_button": "",
        "event_feed_button": "",
        "my_events_button": "",
        "organisation_profile_button": "",
        "new_feature_idea_button": "",
        "i_have_android_button": "",
        "i_have_ios_button": "",
        "download_button": "",
        "follow_button": "",
        "open_button": "",
        "landing_button": "",
        "ios_app_button": "",
        "android_app_button": "",
        "bot_app_button": "",
        "i_am_organisation_button": "",
        "show_vacancies_button": "",
        "change_studlife": "",
        "get_cv": "",
        "cv_sent": "",
        "start_pick_lang": "Language\nЯзык",
    }
}


def local(text, user_id):
    global translations
    lang = db.get_lang(user_id)
    try:
        translated_text = translations[lang][text]
        if translated_text == "":
            translated_text = translations["ru"][text]
        return translated_text
    except Exception as e:
        logging.error(str(e))
        return text
