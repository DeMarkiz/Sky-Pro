import os
import json


def read_transactions(file_path):
    """
    Читает JSON-файл и возвращает список транзакций.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.
    """
    # Проверка существования файла
    if not os.path.exists(file_path):
        return []

    try:
        # Открытие и чтение файла
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Проверка, что содержимое файла - список
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, FileNotFoundError):
        # Обработка ошибок: некорректный JSON или файл не найден
        return []
