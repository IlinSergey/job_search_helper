from telegram import Update
from telegram.ext.filters import UpdateFilter

from data_base.user import create_user, is_user_in_db


class FilterIsUser(UpdateFilter):
    def filter(self, update: Update) -> bool:  # noqa: A003
        if is_user_in_db(update.effective_user):  # type: ignore [arg-type]
            return True
        create_user(update.effective_user, update.message.chat_id)  # type: ignore [arg-type]
        return True
