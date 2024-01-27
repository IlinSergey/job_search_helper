from telegram.ext import CallbackContext

from data_base.search_params import get_search_params
from data_base.vacancy import read_vacancy
from services.hh import HHAgent
from utils.keyboards import covering_letter_keyboard

hh = HHAgent()


async def update_db(context: CallbackContext) -> None:
    user_id = context._user_id
    search_params = get_search_params(user_id)  # type: ignore [arg-type]
    if search_params:
        hh.find_vacation(search_params, user_id)  # type: ignore [arg-type]


async def send_vacation(context: CallbackContext) -> None:
    chat_id, user_id = context._chat_id, context._user_id
    vacancy_data = read_vacancy(user_id)  # type: ignore [arg-type]
    if vacancy_data:
        vacancy, vacancy_id = vacancy_data
        if user_id == 1055229700:
            keyboard = covering_letter_keyboard(vacancy_id)
        else:
            keyboard = None
        await context.bot.send_message(chat_id=chat_id, text=vacancy, reply_markup=keyboard)
    else:
        pass
