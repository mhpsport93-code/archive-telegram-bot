from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import internetarchive

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

async def upload(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    path = "upload_file"

    await file.download_to_drive(path)

    identifier = "tg_upload_" + str(update.message.message_id)

    internetarchive.upload(
        identifier,
        files={path: path},
        metadata={"title": identifier, "mediatype": "movies"}
    )

    link = f"https://archive.org/details/{identifier}"

    await update.message.reply_text(f"Uploaded ✅\n{link}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.Document.ALL, upload))

app.run_polling()
