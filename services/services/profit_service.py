from services.orders_service import get_orders

def calculate_profit():
    orders = get_orders()
    total_profit = sum(order["profit"] for order in orders)
    return total_profit
