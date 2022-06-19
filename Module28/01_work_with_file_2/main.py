class Open:
    def __init__(self, name) -> None:
        self.file_name = name
        self.open_file = None

    def write(self, *args) -> None:
        if args:
            self.open_file.write(str(args))
        else:
            text = input('Что запишем в файл?\n')
            self.open_file.write(text)

    def __enter__(self) -> 'Open':
        print(f'Открываем файл {self.file_name}')
        self.open_file = open(self.file_name, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.open_file.close()
        print(f'Файл {self.file_name} закрыт.')


with Open('test_2.py') as file:
    file.write()
