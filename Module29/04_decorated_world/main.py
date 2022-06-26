from collections.abc import Callable
from typing import Any


def decorator_with_args_for_any_decorator(*args, **kwargs) -> Any:
    print(f'Переданные арги и кварги в декоратор: {args} {kwargs}')

    def decorated_decorator(func: Callable) -> Any:
        def wrapp(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrapp
    return decorated_decorator


@decorator_with_args_for_any_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
