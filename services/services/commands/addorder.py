from telegram import Update
from telegram.ext import ContextTypes
from services.orders_service import add_order

async def addorder_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if len(context.args) < 3:
            await update.message.reply_text("Использование: /addorder <товар> <цена> <себестоимость>")
            return

        product = context.args[0]
        price = float(context.args[1])
        cost = float(context.args[2])

        order = add_order(product, price, cost)
        await update.message.reply_text(
            f"Заказ добавлен:\nТовар: {order['product']}\nЦена: {order['price']}\nСебестоимость: {order['cost']}\nПрибыль: {order['profit']}"
        )
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")
