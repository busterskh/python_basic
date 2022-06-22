import functools
from typing import Callable, Any

app = dict()


def callback(text: str = None) -> Callable:

    def decorator(func: Callable) -> Any:
        @functools.wraps(func)
        def wrapp(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrapp
    app[text] = decorator
    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = example()
    print('Ответ:', response)
else:
    print('Такого пути нет')
