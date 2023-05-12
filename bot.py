from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

from config import TG_TOKEN
from hh import HHAgent
from utils import covering_letter
from openai import get_covering_letter

hh = HHAgent()


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


async def find_vacations(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    hh.find_vacation()
    await update.message.reply_text("База вакансий обновлена!")


async def show_vacations(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    vacation = hh.get_vacantion()
    keyboard = covering_letter(vacation[1])
    await update.message.reply_text(vacation[0], reply_markup=keyboard)


async def letter(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:    
    await update.callback_query.message.reply_text("Готовим сопроводительное письмо...")
    query = update.callback_query
    await query.answer()
    vacancy_id = update.callback_query.data
    vacation_full_description = hh.get_description_about_vacation(int(vacancy_id))
    letter = get_covering_letter(vacation_full_description)
    await update.callback_query.message.reply_text(letter)


def main():
    app = ApplicationBuilder().token(TG_TOKEN).build()

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("find", find_vacations))
    app.add_handler(CommandHandler("show", show_vacations))
    app.add_handler(CallbackQueryHandler(letter))

    app.run_polling()


if __name__ == "__main__":
    main()
