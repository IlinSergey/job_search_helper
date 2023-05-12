from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import TG_TOKEN
from hh import HHAgent

hh = HHAgent()


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


async def find_vacations(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    hh.find_vacation()
    await update.message.reply_text("База вакансий обновлена!")


async def show_vacations(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    vacation = hh.get_vacantion()
    await update.message.reply_text(vacation)


def main():
    app = ApplicationBuilder().token(TG_TOKEN).build()

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("find", find_vacations))
    app.add_handler(CommandHandler("show", show_vacations))

    app.run_polling()


main()
