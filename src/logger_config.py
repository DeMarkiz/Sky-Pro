import logging
import os


def setup_logger(name: str) -> logging.Logger:
    """
    Настраивает логгер с заданным именем.

    :param name: Имя логгера.
    :return: Настроенный логгер.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Создание директории для логов, если она не существует
    logs_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_dir, exist_ok=True)

    # Определение пути к файлу логов
    log_file = os.path.join(logs_dir, f"{name}.log")

    # Создание обработчика для записи логов в файл
    file_handler = logging.FileHandler(log_file, mode="w")
    file_handler.setLevel(logging.DEBUG)

    # Создание форматера с параметрами: дата/время, имя логера, уровень, сообщение
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
    file_handler.setFormatter(formatter)

    # Добавление обработчика к логгеру
    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger
