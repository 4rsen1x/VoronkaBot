from aiogram import types
from advanced_localization import local
from load_config import *


def main_menu(user_id):
    main_kb = [
        [types.KeyboardButton(text=local("about_voronka_button", user_id)),
         types.KeyboardButton(text=local("report_problem_button", user_id))],
        [types.KeyboardButton(
            text=local("help_with_promotion_button", user_id))],
        [types.KeyboardButton(text=local("become_partner_button", user_id)),
         types.KeyboardButton(text=local("change_language_button", user_id))]
    ]
    menu = types.ReplyKeyboardMarkup(keyboard=main_kb, resize_keyboard=True)
    return menu


def support_menu(user_id):
    support_kb = [
        [types.KeyboardButton(text=local(
            "change_studlife_button", user_id))],
        [types.KeyboardButton(
            text=local("leave_tip_button", user_id))],
        [types.KeyboardButton(text=local(
            "tell_friends_button", user_id))],
        [types.KeyboardButton(text=local("back_button", user_id))],
    ]
    menu = types.ReplyKeyboardMarkup(
        keyboard=support_kb, resize_keyboard=True)
    return menu


def kopilka_menu(user_id):
    menu = types.InlineKeyboardMarkup()
    kopilka_button = types.InlineKeyboardButton(
        local("our_kopilka_button", user_id), url=KOPILKA_LINK)
    menu.add(kopilka_button)
    return menu


language_menu = types.InlineKeyboardMarkup()
language_button_ru = types.InlineKeyboardButton(
    text="Русский", callback_data="ru")
language_button_en = types.InlineKeyboardButton(
    text="English", callback_data="en")
language_menu.add(language_button_ru)
language_menu.add(language_button_en)


def about_voronka_menu(user_id):
    about_voronka_kb = [
        [types.KeyboardButton(text=local(
            "change_studlife_button", user_id))],
        [types.KeyboardButton(text=local("about_team_button", user_id)),
         types.KeyboardButton(
            text=local("about_service_button", user_id))],
        [types.KeyboardButton(text=local("our_mission_button", user_id))],
        [types.KeyboardButton(text=local("back_button", user_id)),
         types.KeyboardButton(
            text=local("to_begin_button", user_id))]
    ]
    menu = types.ReplyKeyboardMarkup(
        keyboard=about_voronka_kb, resize_keyboard=True)
    return menu


def change_studlife_menu(user_id):
    our_mission_kb = [[types.KeyboardButton(text=local(
        "change_studlife_button", user_id))],
        [types.KeyboardButton(text=local("back_button", user_id)),
         types.KeyboardButton(
            text=local("to_begin_button", user_id))]]
    menu = types.ReplyKeyboardMarkup(
        keyboard=our_mission_kb, resize_keyboard=True)
    return menu


def about_service_menu(user_id):
    about_service_kb = [
        [types.KeyboardButton(text=local("about_features_button", user_id))],
        [types.KeyboardButton(text=local(
            "new_feature_button", user_id))],
        [types.KeyboardButton(text=local("download_app_button", user_id))],
        [types.KeyboardButton(text=local(
            "follow_tg_channel_button", user_id))],
        [types.KeyboardButton(text=local("get_stickers_button", user_id))],
        [types.KeyboardButton(text=local(
            "show_landing_button", user_id))],
        [types.KeyboardButton(text=local("back_button", user_id)),
         types.KeyboardButton(text=local("to_begin_button", user_id))]
    ]
    menu = types.ReplyKeyboardMarkup(
        keyboard=about_service_kb, resize_keyboard=True)
    return menu


def about_features_menu(user_id):
    about_features_kb = [
        [types.KeyboardButton(text=local("pick_interests_button", user_id)),
         types.KeyboardButton(text=local(
             "integrate_elk_button", user_id))],
        [types.KeyboardButton(text=local("event_feed_button", user_id)),
         types.KeyboardButton(text=local(
             "my_events_button", user_id))],
        [types.KeyboardButton(text=local(
            "organisation_profile_button", user_id)),
         types.KeyboardButton(text=local(
             "new_feature_idea_button", user_id))],
        [types.KeyboardButton(text=local("back_button", user_id)),
         types.KeyboardButton(text=local("to_begin_button", user_id))]
    ]
    menu = types.ReplyKeyboardMarkup(
        keyboard=about_features_kb, resize_keyboard=True)
    return menu


def device_menu(user_id):
    device_kb = [
        [types.KeyboardButton(text=local("i_have_android_button", user_id)),
         types.KeyboardButton(text=local(
             "i_have_ios_button", user_id))],
        [types.KeyboardButton(text=local("back_button", user_id)),
         types.KeyboardButton(text=local("to_begin_button", user_id))]]
    menu = types.ReplyKeyboardMarkup(
        keyboard=device_kb, resize_keyboard=True)
    return menu


def inline_download_android(user_id):
    menu = types.InlineKeyboardMarkup()
    download_button = types.InlineKeyboardButton(
        local("download_button", user_id), url=ANDROID_LINK)
    menu.add(download_button)
    return menu


def inline_download_ios(user_id):
    menu = types.InlineKeyboardMarkup()
    download_button = types.InlineKeyboardButton(
        local("download_button", user_id), url=IOS_LINK)
    menu.add(download_button)
    return menu


def inline_tg_channel(user_id):
    menu = types.InlineKeyboardMarkup()
    tg_channel = types.InlineKeyboardButton(
        local("follow_button", user_id), url=IOS_LINK)
    menu.add(tg_channel)
    return menu


def inline_landing_link(user_id):
    menu = types.InlineKeyboardMarkup()
    landing_link = types.InlineKeyboardButton(
        local("open_button", user_id), url=LANDING_LINK)
    menu.add(landing_link)
    return menu


def error_report_menu(user_id):
    error_report_kb = [
        [types.KeyboardButton(text=local("landing_button", user_id)),
         types.KeyboardButton(text=local(
             "ios_app_button", user_id))],
        [types.KeyboardButton(text=local("android_app_button", user_id)),
         types.KeyboardButton(text=local(
             "bot_app_button", user_id))],
        [types.KeyboardButton(text=local(
            "i_am_organisation_button", user_id))],
        [types.KeyboardButton(text=local("back_button", user_id)),
         types.KeyboardButton(text=local("to_begin_button", user_id))]]
    menu = types.ReplyKeyboardMarkup(
        keyboard=error_report_kb, resize_keyboard=True)
    return menu


def back_begin_menu(user_id):
    new_feature_kb = [[types.KeyboardButton(text=local("back_button", user_id)),
                       types.KeyboardButton(text=local("to_begin_button", user_id))]]
    menu = types.ReplyKeyboardMarkup(
        keyboard=new_feature_kb, resize_keyboard=True)
    return menu


def studlife_menu(user_id):
    studlife_kb = [
        [types.KeyboardButton(text=local("show_vacancies_button", user_id)),
         types.KeyboardButton(text=local("tell_friends_button", user_id))],
        [types.KeyboardButton(text=local("back_button", user_id)),
         types.KeyboardButton(text=local("to_begin_button", user_id))]
    ]
    menu = types.ReplyKeyboardMarkup(
        keyboard=studlife_kb, resize_keyboard=True)
    return menu
