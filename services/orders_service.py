import json
from datetime import datetime
import os

ORDERS_FILE = "orders.json"

def load_orders():
    if not os.path.exists(ORDERS_FILE):
        return []
    with open(ORDERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_orders(orders):
    with open(ORDERS_FILE, "w", encoding="utf-8") as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)

def add_order(product, price, cost):
    orders = load_orders()
    profit = price - cost
    order = {
        "id": len(orders) + 1,
        "product": product,
        "price": price,
        "cost": cost,
        "profit": profit,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    orders.append(order)
    save_orders(orders)
    return order

def get_orders():
    return load_orders()
