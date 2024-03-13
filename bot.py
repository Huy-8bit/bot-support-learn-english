from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from nlp import talk

import os


chat_histories = []


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


async def log_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user = update.effective_user
    chat_id = update.message.chat_id
    text = update.message.text


# async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     user = update.effective_user
#     chat_id = update.message.chat_id
#     text = update.message.text
#     response = talk(text)
#     await update.message.reply_text(response)

#     print(f"Message from {user.first_name} (chat_id={chat_id}): {text}")


conversation_history = []


def saveTalking(user, bot):
    # Cập nhật hàm này để thêm vào lịch sử trò chuyện
    conversation_history.append(f"User: {user}\n")
    conversation_history.append(f"Bot: {bot}\n")
    with open("talking.txt", "a") as f:
        f.write(f"User: {user}\n")
        f.write(f"Bot: {bot}\n")
        f.write("\n")


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    chat_id = update.message.chat_id
    text = update.message.text
    response = talk(text, conversation_history)
    saveTalking(text, response)
    await update.message.reply_text(response)


app = (
    ApplicationBuilder().token("7164268885:AAFCfDuosc3vJFctpxSfVV_5iZkcH2R5E0s").build()
)


app.add_handler(CommandHandler("hello", hello))


app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
