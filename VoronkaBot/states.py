from aiogram.dispatcher.filters.state import StatesGroup, State


class NewFeatureStates(StatesGroup):
    new_feature = State()


class ErrorStates(StatesGroup):
    platform = State()
    report = State()


class MenuStates(StatesGroup):
    our_mission = State()
    about_voronka = State()
    about_service = State()
    issue_request = State()
    app_development = State()
    become_partner = State()
    about_team = State()
    change_stud_life = State()
    about_features = State()
    new_feature = State()
    download_app = State()
    support_project = State()
