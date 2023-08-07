import logging
from db_class import db
translations = {
    "en": {
        "Язык выбран!": "",
        "Привет это бот воронки!": "",
        "Стать партнером": "",
        "Если вы хотите стать партнером Воронки, можете связаться с CEO: @shvetsov_07, который с радостью ответит на все интересующие вопросы": "",
        "Как я могу помочь с развитием приложения?": "",
        "Выберите вариант из меню": "",
        "Хочу пополнить баланс копилки на кофе или комплекс команде!": "",
        "Вау! Мы очень рады, спасибо тебе большое)) Вот ссылка на нашу копилку": "",
        "Хочу рассказать о вас друзьям!": "",
        """Это лучшая помощь для нас, спасибо тебе!
Вот небольшое сообщение, которое ты можешь переслать своим друзьям:
привет, хочу поделиться с тобой сервисом о студлайфе вышки! Ребята сделали приложение, которое помогает найти ивент по твоим интересам и зарегистрироваться на него.
Подписывайся на их телеграм-канал, скачивай приложение в AppStore или PlayMarket, а еще забирай крутой стикерпак!
""": "",

    }
}


def local(text, user_id):
    lang = db.get_lang(user_id)
    if lang == "ru":
        return text
    else:
        global translations
        try:
            return translations[lang][text]
        except Exception as e:
            logging.error(str(e))
            return text


def ghl(text):
    global translations
    try:
        eng_ver = translations["en"][text]
        return [text, eng_ver]
    except Exception as e:
        logging.error(str(e))
        return [text, text]
