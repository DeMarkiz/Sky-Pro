# Banking Operations Widget Backend Server

## Description

Server-side for the banking operations widget, designed for integration into the personal account of a major bank's customer. The widget displays the customer's most recent successful transactions.

## Dependencies

- Python 3.8+
- requests 2.32.3
- flake8 3.8.1
- mypy 0.4.3

## Installation

1. Clone the repository:
```
git clone git@github.com:ZorinVS/transactions-widget.git
```
2. Install the dependencies:
```bash
poetry install
```

## Project Testing

The project testing is conducted using the tests package, which includes the following files:
- init.py
- conftest.py
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