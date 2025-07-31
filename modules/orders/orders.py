ORDERS = []

def create_order(user_id, product):
    order = {
        "user_id": user_id,
        "product": product,
        "status": "новый"
    }
    ORDERS.append(order)
    return order
