from telegram import Update
from telegram.ext import ContextTypes
from services.binance_service import get_balance

async def balance_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        balances = get_balance()
        if not balances:
            await update.message.reply_text("Баланс пуст или ключи не настроены.")
            return

        msg = "Баланс Binance:\n"
        for b in balances:
            msg += f"{b['asset']}: {b['free']} (locked: {b['locked']})\n"
        await update.message.reply_text(msg)

    except Exception as e:
        await update.message.reply_text(f"Ошибка получения баланса: {e}")
