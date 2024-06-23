import os
from typing import Dict


def get_mask_card_number(card_number: str) -> str:
    """Возвращает маскированный номер карты в формате XXXX XX** **** XXXX"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Возвращает маскированный номер счета в формате **XXXX"""
    return f"**{account[-4:]}"


def count_files_and_folders(directory_path: str = "", recursive: bool = False) -> Dict[str, int]:
    """Подсчитывает количество файлов и папок в заданной директории"""

    # Нахождение текущего пути
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Выбор директории, в которой будет производиться сканирование
    # Если путь не указан или указан неверно, то используется путь текущей директории
    if not directory_path and not os.path.isdir(directory_path):
        directory_path = current_directory
    # Иначе формируем абсолютный путь для сканирования
    else:
        directory_path = os.path.join(current_directory, directory_path)

    # Счетчики для подсчета количества папок и файлов
    files_count = 0
    folders_count = 0

    def scan_directory(path: str) -> None:
        # Используем для работы с переменными, определенными в функции count_files_and_folders
        nonlocal files_count, folders_count

        with os.scandir(path) as scan:
            for entry in scan:
                if entry.is_file():
                    files_count += 1
                elif entry.is_dir():
                    folders_count += 1
                    # Если recursive = True, то запускаем сканирование вложенных директорий
                    if recursive:
                        scan_directory(entry.path)

    # Запускаем сканирование
    scan_directory(directory_path)

    return {"files": files_count, "folders": folders_count}

print(mask_account_card("Visa Platinum 7000 7922 8960 6361 "))