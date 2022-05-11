def move(n, x, storage, y):
    if n <= 0:
        return
    move(n - 1, x, y, storage)
    print("Переложить диск", n, "со стержня номер", x, "на стержень номер", y)
    move(n - 1, storage, x, y)


numbers = int(input('Введите количество дисков: '))
move(numbers, 1, 2, 3)
