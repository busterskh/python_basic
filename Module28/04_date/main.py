from typing import Any


class Date:
    """
    Класс, реализует вывод даты в формате dd-mm-yyyy, преобразуя его из строки.
    Проверяет валидность даты.
    Функции:
        from_string - получает на вход строку с датой в формате dd-mm-yyyy (str_date),
        запускает проверку валидности, если дата верная, возвращает инициированный класс с датой;

        is_date_valid - получает на вход строку с датой в формате dd-mm-yyyy (str_date),
        проверяет валидность даты и возвращает True или False.
    """

    def __init__(self, year, month, day) -> None:
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def is_date_valid(cls, str_date: str) -> bool:
        list_date = str_date.split('-')
        if 0 < int(list_date[1]) <= 12:
            if int(list_date[1]) in [1, 3, 5, 7, 8, 10, 12] and 0 < int(list_date[0]) <= 31:
                return True
            elif int(list_date[1]) == 2 and 0 < int(list_date[0]) <= 28:
                return True
            elif int(list_date[1]) in [4, 6, 9, 11] and 0 < int(list_date[0]) <= 30:
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def from_string(cls, str_date: str) -> Any:
        if cls.is_date_valid(str_date=str_date):
            list_date = str_date.split('-')
            year = list_date[2]
            month = list_date[1]
            day = list_date[0]
            return Date(year, month, day)
        else:
            return 'Не корректная дата'

    def __str__(self) -> str:
        return f'День: {self.day}\t\tМесяц: {self.month}\t\tГод: {self.year}'


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
