import time
import functools
from typing import Callable, Any


def slowdown(func) -> Callable:
    """ Декоратор. Замедляет выполнение программы на 2 секунды. """

    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        time.sleep(2)
        value = func(*args, **kwargs)
        return value
    return wrapped


@slowdown
def test() -> None:
    """ Простая функция. Выводит текст в консоль."""

    print('<Тут что-то происходит...>')


test()
