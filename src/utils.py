import csv
import json
import os
import re
from typing import Any, Dict, Hashable, List
from collections import Counter

import openpyxl
import pandas as pd

from src.logger_config import setup_logger

# Создание и получение именованного логгера
utils_logger = setup_logger(__name__)


def read_transactions_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к json-файлу.
    :return: Список транзакций.
    """
    if not os.path.exists(file_path):
        utils_logger.warning(f"File does not exist: {file_path}")
        return []

    try:
        with open(file_path) as file:
            data = json.load(file)
            if isinstance(data, list):
                utils_logger.info(f"Successfully read file: {file_path}")
                return data
            else:
                utils_logger.warning(f"Invalid data format in file: {file_path}")
                return []

    except (json.JSONDecodeError, IOError) as e:
        utils_logger.error(f"Error reading file {file_path}: {e}")
        return []


def read_transactions_csv(file_path: str) -> List[Dict[Hashable, Any]]:
    """
    Читает CSV-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к CSV-файлу.
    :return: Список транзакций.
    """
    if not os.path.exists(file_path):
        utils_logger.warning(f"File does not exist: {file_path}")
        return []

    try:
        df = pd.read_csv(file_path)
        if df.empty or not isinstance(df, pd.DataFrame):
            utils_logger.warning(f"File is empty or not a DataFrame: {file_path}")
            return []
        utils_logger.info(f"Successfully read CSV file: {file_path}")
        return df.to_dict(orient="records")

    except pd.errors.EmptyDataError:
        utils_logger.error(f"EmptyDataError: File is empty: {file_path}")
        return []

    except pd.errors.ParserError:
        utils_logger.error(f"ParserError: Failed to parse file: {file_path}")
        return []

    except Exception as e:
        utils_logger.error(f"Unexpected error: {e}")
        return []


def read_transactions_excel(file_path: str) -> List[Dict[Hashable, Any]]:
    """
    Читает Excel-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к Excel-файлу.
    :return: Список транзакций.
    """
    if not os.path.exists(file_path):
        utils_logger.warning(f"File does not exist: {file_path}")
        return []

    try:
        df = pd.read_excel(file_path)
        if df.empty or not isinstance(df, pd.DataFrame):
            utils_logger.warning(f"File is empty or not a DataFrame: {file_path}")
            return []
        utils_logger.info(f"Successfully read Excel file: {file_path}")
        return df.to_dict(orient="records")

    except pd.errors.EmptyDataError:
        utils_logger.error(f"EmptyDataError: File is empty: {file_path}")
        return []

    except ValueError:
        utils_logger.error(f"ValueError: Failed to parse file: {file_path}")
        return []

    except Exception as e:
        utils_logger.error(f"Unexpected error: {e}")
        return []


def search_transactions(transactions, search_string):
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]


def count_transactions_by_category(transactions, categories):
    counter = Counter()
    for transaction in transactions:
        description = transaction.get('description', '')
        for category in categories:
            if category in description:
                counter[category] += 1
    return dict(counter)


def load_transactions_from_json(file_path='data/operations.json'):
    if not os.path.isfile(file_path):
        print(f"Ошибка: {file_path} не является файлом.")
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            transactions = json.load(f)
            if not isinstance(transactions, list):
                return []
            return transactions
    except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
        print(f"Ошибка при загрузке файла: {e}")
        return []


def load_transactions_from_csv(file_path='data/transactions.csv'):
    if not os.path.isfile(file_path):
        print(f"Ошибка: {file_path} не является файлом.")
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            transactions = list(reader)
            return transactions
    except (FileNotFoundError, csv.Error, PermissionError) as e:
        print(f"Ошибка при загрузке файла: {e}")
        return []


def load_transactions_from_xlsx(file_path='data/transactions_excel.xlsx'):
    if not os.path.isfile(file_path):
        print(f"Ошибка: {file_path} не является файлом.")
        return []
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        transactions = []
        headers = [cell.value for cell in sheet[1]]
        for row in sheet.iter_rows(min_row=2, values_only=True):
            transaction = {headers[i]: row[i] for i in range(len(headers))}
            transactions.append(transaction)
        return transactions
    except (FileNotFoundError, openpyxl.utils.exceptions.InvalidFileException, PermissionError) as e:
        print(f"Ошибка при загрузке файла: {e}")
        return []
