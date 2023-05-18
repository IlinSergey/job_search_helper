from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

from config import TG_TOKEN
from data_base import create_user
from hh import HHAgent
from utils import covering_letter
from jobs import update_db


from openai import get_covering_letter

hh = HHAgent()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    create_user(update.effective_user, update.message.chat_id)
    await update.message.reply_text(f"Привет {update.effective_user.first_name}")


async def find_vacations(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    hh.find_vacation()
    await update.message.reply_text("База вакансий обновлена!")


async def show_vacations(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    vacation = hh.get_vacantion()
    if vacation:
        keyboard = covering_letter(vacation[1])
        await update.message.reply_text(vacation[0], reply_markup=keyboard)
    else:
        await update.message.reply_text("Все вакансии просмотрены.")


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

    jq = app.job_queue
    jq.run_repeating(update_db, 3600)

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("find", find_vacations))
    app.add_handler(CommandHandler("show", show_vacations))
    app.add_handler(CallbackQueryHandler(letter))

    app.run_polling()


if __name__ == "__main__":
    main()
