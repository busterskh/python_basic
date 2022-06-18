import functools
from typing import Callable, Any


def debug(func) -> Callable:
    """
    Декоратор. При каждом вызове декорируемой функции
    выводит её имя (вместе со всеми передаваемыми аргументами),
    а затем — какое значение она возвращает.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        k_args = []
        if args:
            for i in args:
                k_args.append(repr(i))

        if kwargs:
            info = dict(**kwargs)
            for key, value in info.items():
                item = str(key) + "=" + repr(value)
                k_args.append(item)

        result = func(*args, **kwargs)

        print('\nВызывается {f_name}({k_args})\n'
              '{r_name} вернула значение {value}'.format(f_name=func.__name__,
                                                         k_args=', '.join(k_args),
                                                         r_name=repr(func.__name__),
                                                         value=repr(result)))
        return print(result)
    return wrapper


@debug
def greeting(name, age=None) -> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
