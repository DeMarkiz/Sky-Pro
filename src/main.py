import csv
import json
import os
from datetime import datetime
import openpyxl
import utils


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
            reader = csv.DictReader(f, delimiter=';')
            transactions = []
            for row in reader:
                row['operationAmount'] = {
                    'amount': row.pop('amount', 'Не указана'),
                    'currency': {
                        'name': row.pop('currency_name', 'Не указана'),
                        'code': row.pop('currency_code', 'Не указана')
                    }
                }
                transactions.append(row)
            return transactions
    except (FileNotFoundError, csv.Error, PermissionError) as e:
        print(f"Ошибка при загрузке файла: {e}")
        return []


def load_transactions_from_xlsx(file_path='data/transactions_excel.xlsx'):
    """Загрузка транзакций из XLSX-файла"""
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
            # Ensure amount and currency_code are inside a nested dictionary like JSON
            transaction['operationAmount'] = {
                'amount': transaction.pop('amount', 'Не указана'),
                'currency': {
                    'name': transaction.pop('currency_name', 'Не указана'),
                    'code': transaction.pop('currency_code', 'Не указана')
                }
            }
            transactions.append(transaction)
        return transactions
    except (FileNotFoundError, openpyxl.utils.exceptions.InvalidFileException, PermissionError) as e:
        print(f"Ошибка при загрузке файла: {e}")
        return []


def filter_transactions_by_status(transactions, status):
    status = status.lower()
    filtered = []
    for transaction in transactions:
        state = transaction.get('state')
        if state and state.lower() == status:
            filtered.append(transaction)
    return filtered


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    user_input = input("Пользователь: ").strip()

    if user_input == '1':
        print("Для обработки выбран JSON-файл.")
        transactions = load_transactions_from_json()
    elif user_input == '2':
        print("Для обработки выбран CSV-файл.")
        transactions = load_transactions_from_csv()
    elif user_input == '3':
        print("Для обработки выбран XLSX-файл.")
        transactions = load_transactions_from_xlsx()
    else:
        print("Данный тип файлов пока не поддерживается.")
        return

    if not transactions:
        print("Не удалось загрузить транзакции. Проверьте файл и повторите попытку.")
        return

    print(f"Загружено {len(transactions)} транзакций.")

    valid_statuses = ['executed', 'canceled', 'pending']

    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию"
                       " (EXECUTED, CANCELED, PENDING): ").strip().lower()
        if status in valid_statuses:
            break
        else:
            print(f"Статус операции \"{status}\" недоступен.")

    filtered_transactions = filter_transactions_by_status(transactions, status)
    print(f"Операции отфильтрованы по статусу \"{status.upper()}\". Найдено {len(filtered_transactions)} транзакций.")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    sort_by_date = input("Отсортировать операции по дате? (Да/Нет): ").strip().lower()
    if sort_by_date == 'да':
        order = input("Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию): ").strip().lower()
        reverse_order = order == 'по убыванию'
        filtered_transactions.sort(key=lambda x: datetime.fromisoformat(x['date'].replace('Z', '+00:00')),
                                   reverse=reverse_order)

    only_rub = input("Выводить только рублевые транзакции? (Да/Нет): ").strip().lower() == 'да'
    if only_rub:
        filtered_transactions = [t for t in filtered_transactions if t.get('operationAmount',
                                                                           {}).get('currency',
                                                                                   {}).get('code', '').lower() == 'rub']

    filter_description = input("Отфильтровать список транзакций по определенному слову в описании? "
                               "(Да/Нет): ").strip().lower()
    if filter_description == 'да':
        search_string = input("Введите строку для поиска в описании: ").strip()
        filtered_transactions = utils.search_transactions(filtered_transactions, search_string)

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")
        for transaction in filtered_transactions:
            date = transaction.get('date', 'Не указана')
            description = transaction.get('description', 'Не указано')
            from_account = transaction.get('from', 'Не указано')
            to_account = transaction.get('to', 'Не указано')
            amount = transaction.get('operationAmount', {}).get('amount', 'Не указана')
            currency = transaction.get('operationAmount', {}).get('currency', {}).get('code', 'Не указана').upper()
            print(f"{date} {description}\n"
                  f"Счет: {from_account} -> {to_account}\n"
                  f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
