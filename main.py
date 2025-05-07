import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

positions = [
    ("Top-Left", "top-left"),
    ("Top-Center", "top-center"),
    ("Top-Right", "top-right"),
    ("Center-Left", "center-left"),
    ("Center", "center"),
    ("Center-Right", "center-right"),
    ("Bottom-Left", "bottom-left"),
    ("Bottom-Center", "bottom-center"),
    ("Bottom-Right", "bottom-right")
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(pos[0], callback_data=pos[1])]
        for pos in positions
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose logo position:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Selected position: {query.data}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
