import unittest
from unittest.mock import patch, mock_open
import os
import json
from src.utils import read_transactions


def test_read_transactions():
    with patch("builtins.open", mock_open(read_data='[{"amount": 100, "currency": "USD"}]')):
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            result = read_transactions("path/to/operations.json")
            assert result == [{"amount": 100, "currency": "USD"}]

def test_read_transactions_file_not_exists():
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = False
        result = read_transactions("path/to/nonexistent.json")
        assert result == []

def test_read_transactions_not_list():
    with patch("builtins.open", mock_open(read_data='{}')):
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            result = read_transactions("path/to/operations.json")
            assert result == []

def test_read_transactions_empty_file():
    with patch("builtins.open", mock_open(read_data='')):
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            result = read_transactions("path/to/empty.json")
            assert result == []

def test_read_transactions_invalid_json():
    with patch("builtins.open", mock_open(read_data='invalid json')):
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            result = read_transactions("path/to/invalid.json")
            assert result == []

if __name__ == '__main__':
    test_read_transactions()
    test_read_transactions_file_not_exists()
    test_read_transactions_not_list()
    test_read_transactions_empty_file()
    test_read_transactions_invalid_json()
    print("All tests passed.")
