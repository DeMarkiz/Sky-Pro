import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATES_API_KEY')
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_currency(amount, currency):
    """
    Конвертирует сумму из заданной валюты в рубли с использованием внешнего API.
    """
    if currency == "RUB":
        return float(amount)

    params = {
        "to": "RUB",
        "from": currency,
        "amount": amount
    }

    headers = {
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    data = response.json()

    if response.status_code == 200 and data.get('success'):
        return float(data['result'])
    else:
        raise ValueError("Error in converting currency")


def get_transaction_amount_in_rub(transaction):
    """
    Возвращает сумму транзакции в рублях.
    """
    amount = transaction.get('amount', 0)
    currency = transaction.get('currency', 'RUB')

    return convert_currency(amount, currency)
