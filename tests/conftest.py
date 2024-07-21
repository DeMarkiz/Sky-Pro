from typing import Any, Dict, List, Union

import pytest


@pytest.fixture
def card_number() -> str:
    """
    Фикстура для предоставления замаскированного номера карты.

    :return: Маскированный номер карты в формате XXXX XX** **** XXXX.
    """
    return "7000 79** **** 6361"


@pytest.fixture
def ISO_8601() -> str:
    """
    Фикстура для предоставления строки с датой в нужном формате.

    :return: Строка с датой в виде dd.mm.yyyy.
    """
    return "11.07.2018"


@pytest.fixture
def records_ascending() -> List[Dict[str, Union[int, str]]]:
    """
    Фикстура для предоставления отсортированного списка операций по возрастанию.

    :return: Отсортированный список операций.
    """
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def records_descending() -> List[Dict[str, Union[int, str]]]:
    """
    Фикстура для предоставления отсортированного списка операций по убыванию.

    :return: Отсортированный список операций.
    """
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def transaction_descriptions_list() -> List[str]:
    """
    Фикстура для предоставления описания для каждой операции.

    :return: Список описаний операций.
    """
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    """
    Фикстура для предоставления тестовых данных о финансовых транзакциях.

    :return: Список словарей с данными о транзакциях.
    """
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "100000", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]