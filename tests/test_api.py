import unittest
from unittest.mock import patch, Mock
from src.external_api import convert_currency, get_transaction_amount_in_rub


def test_convert_currency():
    with patch('requests.get') as mock_get:
        # Мокируем ответ API
        mock_response = Mock()
        expected_result = 75.0
        mock_response.json.return_value = {
            "success": True,
            "result": expected_result
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        amount = 1.0
        currency = "USD"
        result = convert_currency(amount, currency)
        assert result == expected_result

        # Тестируем конвертацию, если валюта - RUB
        assert convert_currency(100, "RUB") == 100.0


def test_get_transaction_amount_in_rub():
    with patch('requests.get') as mock_get:
        # Мокируем ответ API
        mock_response = Mock()
        mock_response.json.return_value = {
            "success": True,
            "result": 100.0
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        transaction = {
            "amount": 1.0,
            "currency": "USD"
        }
        result = get_transaction_amount_in_rub(transaction)
        assert result == 100.0

        # Тестируем, когда валюта - RUB
        transaction = {
            "amount": 100.0,
            "currency": "RUB"
        }
        result = get_transaction_amount_in_rub(transaction)
        assert result == 100.0


if __name__ == '__main__':
    test_convert_currency()
    test_get_transaction_amount_in_rub()
    print("All tests passed.")
