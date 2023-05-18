from telegram.ext import CallbackContext

from hh import HHAgent


hh = HHAgent()


async def update_db(context: CallbackContext) -> None:
    hh.find_vacation()


