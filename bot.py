from warnings import filterwarnings

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (ApplicationBuilder, CallbackQueryHandler,
                          CommandHandler, ContextTypes, ConversationHandler,
                          MessageHandler, filters)
from telegram.warnings import PTBUserWarning

from anketa import anketa_start, save_vacancy
from config import TG_TOKEN
from data_base import (create_table_user, create_table_vacation, create_user,
                       is_user)
from hh import HHAgent
from jobs import send_vacation, update_db
from yagpt import get_covering_letter

filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)


hh = HHAgent()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    create_table_user()
    create_table_vacation()
    if not is_user(update.effective_user.id):
        create_user(update.effective_user, update.message.chat_id)
    keyboard = [
        [
            InlineKeyboardButton("Заполнить анкету", callback_data="анкета")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"Привет {update.effective_user.first_name}, для успешного поиска вакансий, необходимо заполнить анкету",
                                    reply_markup=reply_markup)


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
    vacation_full_description = hh.get_description_about_vacation(int(vacancy_id))
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
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("run", run))
    app.add_handler(CommandHandler("stop", stop))

    app.add_handler(CallbackQueryHandler(letter))

    app.run_polling()


if __name__ == "__main__":
    main()
