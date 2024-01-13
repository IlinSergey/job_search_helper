from warnings import filterwarnings

from telegram import Update
from telegram.ext import (ApplicationBuilder, CallbackQueryHandler,
                          CommandHandler, ContextTypes, ConversationHandler,
                          MessageHandler, filters)
from telegram.warnings import PTBUserWarning

from data_base.models import create_tables
from services.hh import HHAgent
from services.jobs import send_vacation, update_db
from services.yagpt import get_covering_letter
from utils.anketa import anketa_start, save_vacancy
from utils.config import TG_TOKEN
from utils.custom_filtesrs import FilterIsUser
from utils.keyboards import START_KEYBOARD

filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)


hh = HHAgent()
is_user_filter = FilterIsUser()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Привет {update.effective_user.first_name},"
                                    f" для успешного поиска вакансий, необходимо заполнить анкету",
                                    reply_markup=START_KEYBOARD)


async def run(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id, user_id = update.effective_message.chat_id, update.effective_user.id
    context.job_queue.run_repeating(send_vacation, chat_id=chat_id, user_id=user_id, interval=10, first=5)
    context.job_queue.run_repeating(update_db, user_id=user_id, interval=60, first=1)
    await update.message.reply_text("Начинаем периодический поиск и рассылку подходящих вакансий")


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    current_jobs = context.job_queue.jobs()
    if not current_jobs:
        await update.message.reply_text("Ничего не запущено")
    for job in current_jobs:
        job.schedule_removal()
    await update.message.reply_text("Автоматический поиск остановлен")


async def letter(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.message.reply_text("Готовим сопроводительное письмо, это займет какое-то время...")
    query = update.callback_query
    await query.answer()
    vacancy_id = update.callback_query.data
    if vacancy_id is not None:
        vacation_full_description = hh.get_description_about_vacation(int(vacancy_id))
    if isinstance(vacation_full_description, str):
        letter = get_covering_letter(vacation_full_description)
    await update.callback_query.message.reply_text(letter)


def main():
    app = ApplicationBuilder().token(TG_TOKEN).build()

    anketa = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(anketa_start, pattern="^(анкета)$")
        ],
        states={
            "vacancy_name": [MessageHandler(filters.TEXT, save_vacancy)]
        },
        fallbacks=[]
    )
    app.add_handler(anketa)
    app.add_handler(CommandHandler("start", start, is_user_filter))
    app.add_handler(CommandHandler("run", run))
    app.add_handler(CommandHandler("stop", stop))

    app.add_handler(CallbackQueryHandler(letter))

    app.run_polling()


if __name__ == "__main__":
    create_tables()
    main()
