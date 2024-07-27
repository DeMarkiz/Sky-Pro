from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования результатов выполнения функции.
    Поведение:
    - Если filename указан, результат выполнения функции будет записан в указанный файл.
    - Если filename не указан, результат выполнения функции будет выведен в консоль.
    :param filename: Путь к файлу, в который будет производиться логирование. По умолчанию None.
    :return: Возвращает обернутую функцию с логированием.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as exc_info:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {str(exc_info)}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {str(exc_info)}. Inputs: {args}, {kwargs}")

        # Установка документации и аннотаций вручную для обернутой функции
        wrapper.__doc__ = func.__doc__
        wrapper.__annotations__ = func.__annotations__

        return wrapper

    return decorator
