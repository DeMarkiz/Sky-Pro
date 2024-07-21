import json
import os
from typing import Any, Dict, Hashable, List

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