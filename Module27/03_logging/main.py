from datetime import datetime
import functools
from typing import Callable, Any


def logging(func) -> Callable:
    """
    Декоратор. Записывает все ошибки декорированных функций в лог-файл.
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        try:
            value = func(*args, **kwargs)
            return value
        except Exception as error:
            with open('function_errors.log', 'a', encoding='utf-8') as log_file:
                log_file.write(f'{datetime.now()};\tИмя: {func.__name__};\tОшибка: {error}\n')
            return
    return wrapped


@logging
def function():
    """ Простая функция. Выдает сумму двух чисел. Намеренно неправильная."""

    a, b = 10, 20
    print(sum(a, b))


@logging
def test() -> None:
    """ Простая функция. Выводит текст в консоль."""

    print('<Тут что-то происходит...>')


@logging
def test_2() -> None:
    """ Простая функция. Выдает сумму двух рандомных чисел от 1 до 100. Намеренно неправильная."""

    a, b = random.randint(1, 100), random.randint(1, 100)
    print(a + b)


function()
test()
test_2()
