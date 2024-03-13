from telegram import Update, Filters
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Xin chào! Tôi là bot của bạn.")


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hãy gửi /start để bắt đầu!")


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(
        "7164268885:AAFCfDuosc3vJFctpxSfVV_5iZkcH2R5E0s", use_context=True
    )

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
