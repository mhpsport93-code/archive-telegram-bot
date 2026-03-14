import os
import internetarchive
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("8659154394:AAFGp3U2HVLd_VxIIMbx32XIRYnKoGu7QmA")
IA_ACCESS_KEY = os.getenv("SHFLEKv9geVL6wG1")
IA_SECRET_KEY = os.getenv("wX8TCn2lga9yhUcQ")

async def upload(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()

    file_path = "upload_file"
    await file.download_to_drive(file_path)

    identifier = "tg_upload_" + str(update.message.message_id)

    internetarchive.upload(
        identifier,
        files={file_path: file_path},
        metadata={
            "title": identifier,
            "mediatype": "movies"
        },
        access_key=IA_ACCESS_KEY,
        secret_key=IA_SECRET_KEY
    )

    link = f"https://archive.org/details/{identifier}"

    await update.message.reply_text(f"Uploaded ✅\n{link}")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.Document.ALL, upload))

print("Bot started...")

app.run_polling()
