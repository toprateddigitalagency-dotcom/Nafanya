PRODUCTS = [
    {"id": 1, "name": "Наушники Gelius NavyStrike", "price": 800},
    {"id": 2, "name": "Очки Xiaomi AR", "price": 4500},
    {"id": 3, "name": "Powerbank Samsung 20 000mAh", "price": 1200}
]

def get_product_list():
    text = "Каталог товаров:\n\n"
    for p in PRODUCTS:
        text += f"{p['id']}. {p['name']} — {p['price']} грн\n"
    text += "\nДля заказа введите: /order <id товара>"
    return text

def find_product(product_id):
    for p in PRODUCTS:
        if p['id'] == product_id:
            return p
    return None
  
