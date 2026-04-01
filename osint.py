import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📱 Send Indian phone number (without +91)")

# Message handler (number input)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phone_number = update.message.text.strip()

    await update.message.reply_text("🔍 Searching details...")

    api_url = f"https://numbeer-info.vercel.app/api/lookup?numbere={phone_number}&key=SH4DAW-D4DY"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            result = "\n📊 *RESULTS:*\n"
            for key, value in data.items():
                result += f"\n🔹 {key.upper()}: {value}"

            await update.message.reply_text(result, parse_mode="Markdown")

        else:
            await update.message.reply_text("❌ API error or invalid key")

    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {e}")

# App setup
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot running...")
app.run_polling()
