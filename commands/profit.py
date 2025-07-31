from telegram import Update
from telegram.ext import ContextTypes
from services.profit_service import calculate_profit

async def profit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    total_profit = calculate_profit()
    await update.message.reply_text(f"Общая прибыль: {total_profit}₴")
