from modules.orders.products import get_product_list, find_product
from modules.orders.orders import create_order
from config import ADMIN_ID
from telebot import TeleBot

def register_order_handlers(bot: TeleBot):

    @bot.message_handler(commands=['products'])
    def send_products(message):
        bot.reply_to(message, get_product_list())

    @bot.message_handler(commands=['order'])
    def order_product(message):
        try:
            product_id = int(message.text.split()[1])
        except (IndexError, ValueError):
            bot.reply_to(message, "Используй формат: /order <id товара>")
            return

        product = find_product(product_id)
        if not product:
            bot.reply_to(message, "Товар не найден.")
            return

        order = create_order(message.from_user.id, product)
        bot.reply_to(message, f"Заказ принят: {product['name']} ({product['price']} грн)")
        bot.send_message(ADMIN_ID, f"Новый заказ!\nПользователь: {message.from_user.username}\nТовар: {product['name']}")
