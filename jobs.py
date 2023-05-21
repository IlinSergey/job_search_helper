from telegram.ext import CallbackContext

from data_base import find_vacancy_name, read_vacantion
from hh import HHAgent
from utils import covering_letter

hh = HHAgent()


async def update_db(context: CallbackContext) -> None:
    user_id = context._user_id
    vacancy_name = find_vacancy_name(user_id)
    hh.find_vacation(vacancy_name, user_id)


async def send_vacation(context: CallbackContext):
    chat_id, user_id = context._chat_id, context._user_id
    vacation = read_vacantion(user_id)
    if vacation:
        if user_id == 1055229700:
            keyboard = covering_letter(vacation[1])
        else:
            keyboard = None
        await context.bot.send_message(chat_id=chat_id, text=vacation[0], reply_markup=keyboard)
    else:
        pass
