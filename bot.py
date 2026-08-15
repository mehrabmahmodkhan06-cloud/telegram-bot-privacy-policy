import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🌙 به MidnightNatureBot خوش آمدید!\n\n"
        "اینجا قراره محتوای طبیعت، شب، ماشین و موسیقی رو با هم داشته باشیم. 🌿🚗🎵"
    )


def main() -> None:
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise RuntimeError("BOT_TOKEN is not set.")

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()


if __name__ == "__main__":
    main()
