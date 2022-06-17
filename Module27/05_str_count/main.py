import functools
from typing import Callable, Any


def counter(func) -> Callable:
    """
    Декоратор. Считает количество вызовов декорируемой функции.
    """

    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        value = func(*args, **kwargs)
        if func.__name__ not in count:
            count[func.__name__] = 0
        count[func.__name__] += 1
        print('Функция {name} была вызвана {count} раз(а)'.format(name=func.__name__,
                                                                  count=count[func.__name__]))
        return value

    return wrapped


@counter
def test() -> None:
    """ Простая функция. Выводит текст в консоль."""

    print('<Тут что-то происходит...>')


@counter
def test_2() -> None:
    print('<Тут тоже что-то происходит...>')


count = dict()

for _ in range(5):
    test()

for _ in range(3):
    test_2()
