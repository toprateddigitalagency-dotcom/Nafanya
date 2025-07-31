from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Команды НАФАНИ:\n"
        "/start – Запуск\n"
        "/help – Справка\n"
        "/balance – Баланс Binance\n"
        "/report – Отчёт по прибыли (в разработке)\n"
        "/strict_on – Включить строгий режим"
    )
    await update.message.reply_text(text)
