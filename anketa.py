from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from data_base.user import set_vacancy


async def anketa_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    if query:
        await query.edit_message_text("Введите текст для поиска вакансии:")
    return "vacancy_name"


async def save_vacancy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text
    set_vacancy(update.effective_user, text)
    await update.message.reply_text(f"Ваканcии будут искаться по запросу {text}")
    return ConversationHandler.END
