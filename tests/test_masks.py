from unittest.mock import Mock, patch

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number: str) -> None:
    """
    Тестирует функцию get_mask_card_number на корректность работы.

    :param card_number: Маскированный номер карты для сравнения, представленный фикстурой.
    :return: None
    """
    assert get_mask_card_number("7000792289606361") == card_number


@patch("src.masks.masks_logger")
def test_get_mask_card_number_logs_info(mock_logger: Mock, card_number: str) -> None:
    """
    Тестирует, что функция get_mask_card_number логирует корректное сообщение.

    :param mock_logger: Замоканный объект логгера.
    :param card_number: Маскированный номер карты для сравнения, представленный фикстурой.
    :return: None
    """
    assert get_mask_card_number("7000792289606361") == card_number
    mock_logger.info.assert_called_once_with(f"Masked card number: {card_number}")


@pytest.mark.parametrize(
    "account, expected",
    [("73654108430135874305", "**4305"), ("72954141430135305679", "**5679"), ("98765432109876543210", "**3210")],
)
def test_get_mask_account(account: str, expected: str) -> None:
    """
    Тестирует функцию get_mask_account на корректность работы с различными входными данными.

    :param account: Номер счета.
    :param expected: Ожидаемый маскированный номер счета.
    :return: None.
    """
    assert get_mask_account(account) == expected


@patch("src.masks.masks_logger")
def test_get_mask_account_logs_info(mock_logger: Mock) -> None:
    """
    Тестирует, что функция get_mask_account логирует корректное сообщение.

    :param mock_logger: Замоканный объект логгера.
    :return: None.
    """
    assert get_mask_account("73654108430135874305") == "**4305"
    mock_logger.info.assert_called_once_with("Masked account number: **4305")