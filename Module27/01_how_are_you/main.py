import random
from typing import Callable, Any
import functools


def how_are_you(func) -> Callable:
    """ Декоратор. Надоедает, прежде чем запустить декорируемую функцию. """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        _ = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        value = func(*args, **kwargs)
        return value
    return wrapped_func


@how_are_you
def test() -> None:
    """ Простая функция. Выводит текст в консоль."""

    print('<Тут что-то происходит...>')


@how_are_you
def test_2() -> None:
    """ Простая функция. Выдает сумму двух рандомных чисел от 1 до 100."""

    a, b = random.randint(1, 100), random.randint(1, 100)
    print(a + b)


test()
print()
test_2()
