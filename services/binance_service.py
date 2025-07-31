import os
from binance.client import Client

# Подключаем API Binance
def get_binance_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    return Client(api_key, api_secret)

def get_balance():
    client = get_binance_client()
    balances = client.get_account()['balances']
    # Выводим только монеты, где есть баланс
    non_zero = [b for b in balances if float(b['free']) > 0 or float(b['locked']) > 0]
    return non_zero
