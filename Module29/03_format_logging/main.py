import functools
import time


def log_methods(date):
    def decorator(cls):
        def wrapp(*args, **kwargs):
            start = time.time()
            with open('logging.log', 'a', encoding='utf=8') as file:
                file.write(f'Запускается {repr(cls.__name__)}. Дата и время запуска:{date}')
            result = cls(*args, **kwargs)
            end = time.time()
            print(f'Завершение {repr(cls.__name__)}, время работы = {round(start - end, 3)}s')
            return result

        return wrapp
    return decorator


def for_all_methods(decorator):
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method in dir(cls):
            if not i_method.startswith('__'):
                cur_method = getattr(cls, i_method)
                decorated_method = decorator(cur_method)
                setattr(cls, i_method, decorated_method)
        return cls
    return decorate


@log_methods("Apr 23 2021 - 21:50:37")
@for_all_methods(log_methods)
class A:
    @classmethod
    def test_sum_1(cls) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("Apr 23 2021 - 21:50:37")
@for_all_methods(log_methods)
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    @classmethod
    def test_sum_2(cls):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
