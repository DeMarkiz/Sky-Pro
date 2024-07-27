from src.decorators import log


def test_log_without_filename(capsys):
    @log()
    def add(x, y):
        return x + y

    add("1", y=2)
    captured = capsys.readouterr()
    assert captured.out == """add error: can only concatenate str (not "int") to str. Inputs: ('1',), {'y': 2}\n"""

    add(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "add ok\n"


def test_log_with_filename(capsys):
    @log(filename="mylog.txt")
    def add(x, y):
        return x + y

    def read_last_line(file_path):
        """Возвращает результат чтения последней строки"""
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()[-1]

    add("1", y=2)
    last_log = read_last_line("mylog.txt")
    assert last_log == """add error: can only concatenate str (not "int") to str. Inputs: ('1',), {'y': 2}\n"""

    add(1, 2)
    last_log = read_last_line("mylog.txt")
    assert last_log == "add ok\n"
