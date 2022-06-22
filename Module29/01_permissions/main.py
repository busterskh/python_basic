import functools
from collections.abc import Callable
from typing import Any


def check_permission(user: str = None) -> Callable:
    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapp(*args, **kwargs) -> Any:
            try:
                if user in user_permissions:
                    result = func(*args, **kwargs)
                    return result
                else:
                    raise PermissionError
            except PermissionError as error:
                print(f'{repr(error)}: У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
                return
        return wrapp
    return decorator


user_permissions = ['admin']


@check_permission(user='admin')
def delete_site() -> None:
    print('Удаляем сайт')


@check_permission(user='user_1')
def add_comment() -> None:
    print('Добавляем комментарий')


delete_site()
add_comment()
