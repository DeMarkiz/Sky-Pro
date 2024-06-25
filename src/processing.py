from datetime import datetime
from typing import List, Dict, Any


def filter_by_state(transactions: List[Dict[str, Any]],
                    state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по заданному состоянию.

    :param transactions: Список словарей с данными о транзакциях.
    :param state: Состояние, по которому нужно фильтровать (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список транзакций.
    """
    return [transaction for transaction in transactions if state == transaction.get("state")]


def sort_by_date(records: list, is_ascending: bool = True) -> list:
    """
    Сортирует операции по возрастанию (по умолчанию).

    :param records: Список операций.
    :param is_ascending: Параметр для сортировки по дате (по умолчанию True - сортировка по возростанию).
    :return: Отсортированный список операций.
    """

    def sort_key(record: dict) -> datetime:
        """
        Используется в качестве ключа сортировки в функции sorted(), извлекая дату из записи.

        :param record: Запись, содержащая дату и время в формате ISO 8601.
        :return: Объект datetime, полученный из строки даты, который используется в качестве ключа сортировки.
        """
        return datetime.strptime(record["date"], "%Y-%m-%dT%H:%M:%S.%f")

    return sorted(records, key=sort_key, reverse=not is_ascending)
