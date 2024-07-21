import json
import os
from typing import Any, Dict, List

from src.logger_config import setup_logger

# Создание и получение именованного логгера
utils_logger = setup_logger(__name__)


def read_transactions_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к json-файлу.
    :return: Список транзакций.
    """
    if not os.path.exists(file_path):
        utils_logger.warning(f"File {file_path} does not exist.")
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