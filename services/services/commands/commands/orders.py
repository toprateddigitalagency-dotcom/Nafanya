from telegram import Update
from telegram.ext import ContextTypes
from services.orders_service import get_orders

async def orders_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    orders = get_orders()
    if not orders:
        await update.message.reply_text("Заказов пока нет.")
        return

    msg = "Список заказов:\n"
    for order in orders:
        msg += f"{order['id']}. {order['product']} - {order['price']}₴ (прибыль {order['profit']}₴)\n"
    await update.message.reply_text(msg)
