from datetime import datetime


def filter_by_state(records: list, state: str = "EXECUTED") -> list:
    """
    Фильтрует операции по заданному состоянию.

    :param records: Список операций.
    :param state: Состояние для фильтрации (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список операций.
    """
    return [record for record in records if state == record.get("state")]


def sort_by_date(records: list, ascending: bool = True) -> list:
    """
    Сортирует операции по возрастанию (по умолчанию).

    :param records: Список операций.
    :param ascending: Параметр для сортировки по дате (по умолчанию True - сортировка по возростанию).
    :return: Отсортированный список операций.
    """

    def sort_key(record: dict) -> datetime:
        """
        Используется в качестве ключа сортировки в функции sorted(), извлекая дату из записи.

        :param record: Запись, содержащая дату и время в формате ISO 8601.
        :return: Объект datetime, полученный из строки даты, который используется в качестве ключа сортировки.
        """
        return datetime.strptime(record["date"], "%Y-%m-%dT%H:%M:%S.%f")

    return sorted(records, key=sort_key, reverse=not ascending)
