# Banking Operations Widget Backend Server
## Description
Server-side for the banking operations widget, designed for integration into the personal account of a major bank's customer. The widget displays the customer's most recent successful transactions.
## Functionality

Banking Operations Widget Backend Server includes the following functional modules:

- decorators.py
- generators.py
- masks.py
- processing.py
- widget.py

### Functional Modules Overview:

#### decorators.py

Purpose:

- log(filename)
  - The log decorator is used for logging the results of a function execution.
  - Behavior:
    - If filename is provided, the result of the function execution will be written to the specified file.
    - If filename is not provided, the result of the function execution will be printed to the console.
  - Accepts an optional filename parameter (default **None**).
    - filename (str): The path to the file where logging will be performed.
  - Returns the wrapped function with logging.

#### generators.py

Purpose:
- filter_by_currency(transactions, code)
  - Accepts a list of transactions and a currency code.
  - Returns an iterator yielding transactions with the specified currency code.
  
- transaction_descriptions(transactions)
  - Accepts a list of transactions.
  - Generates descriptions for each transaction sequentially.
  
- card_number_generator(start, end)
  - Accepts the start and end of the range for card number generation.
  - Returns card numbers in the format XXXX XXXX XXXX XXXX, where X is a digit.
#### masks.py
Purpose:
- get_mask_card_number(card_number)
  - Accepts a card number as a string.
  - Returns a masked card number in the format XXXX XX** **** XXXX.
  
- get_mask_account(account)
  - Accepts an account number as a string.
  - Returns a masked account number in the format **XXXX.
#### processing.py
Purpose:
- filter_by_state(records, state='EXECUTED')
  - Accepts a list of records and an optional state parameter (default 'EXECUTED').
  - Filters operations by the specified state.
  
- sort_by_date(records, ascending=True)
  - Accepts a list of records and an optional ascending parameter for sorting (default: True - ascending order).
  - Sorts operations by date (ascending by default).
#### widget.py
Functionality:
- Importing functions from masks module for masking account and card numbers.
Purpose:
- mask_account_card(card_or_account_inform) -> str:
  - Accepts a string containing information about the card/account type and number.
  - Returns the original string with the masked card/account number.
  
- get_data(date_of_transaction) -> str:
  - Accepts a string in the format 2018-07-11T02:26:18.671407.
  - Returns a string with the date in the format 11.07.2018.
## Dependencies
- Python 3.12
- requests 2.32.3
- flake8 7.0.0
- black 24.4.2
- isort 5.13.2
- mypy 1.10.0
- pytest 8.2.2
- pytest-cov 5.0.0

## Project Testing
The project testing is conducted using the tests package, which includes the following files:
- init.py
- conftest.py
- test_decorators.py
- test_generators.py
- test_masks.py
- test_processing.py
- test_widget.py
### There are two ways to perform project testing:
1. Using PyCharm's terminal:
```bash
pytest tests
```
2. Using PyCharm's functionality:
- Open the **Edit Configurations** window.
- Select **pytest**.
- Specify the directory containing the tests and the project directory.
- Confirm the changes by clicking **Apply** and **OK**.
- Run **pytest in tests**
## Documentation:
For more information please contact...
## License:
This project is licensed under the [MIT License](LICENSE).