import json
from typing import Any, Dict, List
from unittest.mock import Mock, mock_open, patch

from src.utils import read_transactions_json


def test_read_transactions_json_valid_file(transactions: List[Dict[str, Any]]) -> None:
    """
    Тестирует функцию read_transactions_json с существующим JSON-файлом, содержащим корректные данные.

    :param transactions: Список словарей с данными о транзакциях, предоставленный фикстурой.
    :return: None
    """
    # Преобразуем список транзакций в JSON-строку
    json_data = json.dumps(transactions)

    # Используем mock_open для имитации открытия файла и чтения корректных данных
    mocked_open = mock_open(read_data=json_data)
    with patch("builtins.open", mocked_open):
        # Используем patch для имитации os.path.exists и задаем, чтобы она возвращала True
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            # Вызываем тестируемую функцию и проверяем результат
            result = read_transactions_json("dummy_path.json")
            assert result == transactions
            mocked_open.assert_called_once_with("dummy_path.json")


@patch("src.utils.utils_logger")
def test_read_transactions_json_logs_info(mock_logger: Mock, transactions: List[Dict[str, Any]]) -> None:
    """
    Тестирует, что функция read_transactions_json логирует корректное сообщение при успешном чтении файла.

    :param mock_logger: Замоканный объект логгера.
    :param transactions: Список словарей с данными о транзакциях, предоставленный фикстурой.
    :return: None
    """
    # Преобразуем список транзакций в JSON-строку
    json_data = json.dumps(transactions)

    # Используем mock_open для имитации открытия файла и чтения корректных данных
    mocked_open = mock_open(read_data=json_data)
    with patch("builtins.open", mocked_open):
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            # Вызываем тестируемую функцию и проверяем результат
            result = read_transactions_json("dummy_path.json")
            assert result == transactions
            mock_logger.info.assert_called_once_with("Successfully read file: dummy_path.json")


def test_read_transactions_json_invalid_file() -> None:
    """
    Тестирует функцию read_transactions_json с существующим JSON-файлом, содержащим некорректные данные.

    :return: None.
    """
    # Используем mock_open для имитации открытия файла и чтения некорректных данных
    mocked_open = mock_open(read_data='{"invalid": "data"}')
    with patch("builtins.open", mocked_open):
        # Используем patch для имитации os.path.exists и задаем, чтобы она возвращала True
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            # Вызываем тестируемую функцию и проверяем результат
            result = read_transactions_json("dummy_path.json")
            assert result == []
            mocked_open.assert_called_once_with("dummy_path.json")


@patch("src.utils.utils_logger")
def test_read_transactions_json_invalid_format_logs_warning(mock_logger: Mock) -> None:
    """
    Тестирует, что функция read_transactions_json логирует сообщение предупреждение при некорректном формате данных.

    :param mock_logger: Замоканный объект логгера.
    :return: None.
    """
    # Используем mock_open для имитации открытия файла и чтения некорректных данных
    mocked_open = mock_open(read_data='{"invalid": "data"}')
    with patch("builtins.open", mocked_open):
        # Используем patch для имитации os.path.exists и задаем, чтобы она возвращала True
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            # Вызываем тестируемую функцию и проверяем результат
            result = read_transactions_json("dummy_path.json")
            assert result == []
            mock_logger.warning.assert_called_once_with("Invalid data format in file: dummy_path.json")


def test_read_transactions_json_empty_file() -> None:
    """
    Тестирует функцию read_transactions_json с существующим пустым JSON-файлом.

    :return: None
    """
    # Используем mock_open для имитации открытия пустого файла и чтения данных
    mocked_open = mock_open(read_data="")
    with patch("builtins.open", mocked_open):
        # Используем patch для имитации os.path.exists и задаем, чтобы она возвращала True
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            # Вызываем тестируемую функцию и проверяем результат
            result = read_transactions_json("dummy_path.json")
            assert result == []
            mocked_open.assert_called_once_with("dummy_path.json")


def test_read_transactions_json_nonexistent_file() -> None:
    """
    Тестирует функцию read_transactions_json с несуществующим JSON-файлом.

    :return: None
    """
    # Используем patch для имитации os.path.exists и задаем, чтобы она возвращала False
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = False
        # Вызываем тестируемую функцию и проверяем результат
        result = read_transactions_json("dummy_path.json")
        assert result == []
        mock_exists.assert_called_once_with("dummy_path.json")


@patch("src.utils.utils_logger")
def test_read_transactions_json_nonexistent_file_logs_warning(mock_logger: Mock) -> None:
    """
    Тестирует, что функция read_transactions_json логирует сообщение о том, что файл не существует.

    :param mock_logger: Замоканный объект логгера.
    :return None
    """
    # Используем patch для имитации os.path.exists и задаем, чтобы она возвращала False
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = False
        # Вызываем тестируемую функцию и проверяем результат
        result = read_transactions_json("dummy_path.json")
        assert result == []
        mock_logger.warning.assert_called_once_with("File dummy_path.json does not exist.")


def test_read_transactions_json_json_decode_error() -> None:
    """
    Тестирует функцию read_transactions_json с существующим JSON-файлом, содержащим некорректный формат JSON-данных.

    :return: None
    """
    # Используем mock_open для имитации открытия файла и чтения некорректного формата JSON-данных
    mocked_open = mock_open(read_data="invalid json")
    with patch("builtins.open", mocked_open):
        # Используем patch для имитации os.path.exists и задаем, чтобы она возвращала True
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            # Вызываем тестируемую функцию и проверяем результат
            result = read_transactions_json("dummy_path.json")
            assert result == []
            mocked_open.assert_called_once_with("dummy_path.json")


@patch("src.utils.utils_logger")
def test_read_transactions_json_json_decode_error_logs_error(mock_logger: Mock) -> None:
    """
    Тестирует, что функция read_transactions_json логирует сообщение об ошибке при некорректном формате JSON-данных.

    :param mock_logger: Замоканный объект логгера.
    :return None
    """
    # Используем mock_open для имитации открытия файла и чтения некорректного формата JSON-данных
    mocked_open = mock_open(read_data="invalid json")
    with patch("builtins.open", mocked_open):
        # Используем patch для имитации os.path.exists и задаем, чтобы она возвращала True
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            # Вызываем тестируемую функцию и проверяем результат
            result = read_transactions_json("dummy_path.json")
            assert result == []
            mock_logger.error.assert_called_once_with("Error reading file dummy_path.json: Expecting value: line 1 column 1 (char 0)")


def test_read_transactions_json_io_error() -> None:
    """
    Тестирует функцию read_transactions_json с существующим JSON-файлом при возникновении ошибки IOError.

    :return: None
    """
    # Используем контекстный менеджер pathc и аргумент side_effect для имитации открытия файла и генерации исключения
    with patch("builtins.open", side_effect=IOError):
        # Используем patch для имитации os.path.exists и задаем, чтобы она возвращала True
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            # Вызываем тестируемую функцию и проверяем результат
            result = read_transactions_json("dummy_path.json")
            assert result == []
            mock_exists.assert_called_once_with("dummy_path.json")


@patch("src.utils.utils_logger")
def test_read_transactions_json_io_error_logs_error(mock_logger: Mock) -> None:
    """
    Тестирует, что функция read_transactions_json логирует сообщение об ошибке при IOError.

    :param mock_logger: Замоканный объект логгера.
    """
    # Используем контекстный менеджер pathc и аргумент side_effect для имитации открытия файла и генерации исключения
    with patch("builtins.open", side_effect=IOError("Mock IOError")):
        # Используем patch для имитации os.path.exists и задаем, чтобы она возвращала True
        with patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            # Вызываем тестируемую функцию и проверяем результат
            result = read_transactions_json("dummy_path.json")
            assert result == []
            mock_logger.error.assert_called_once_with("Error reading file dummy_path.json: Mock IOError")