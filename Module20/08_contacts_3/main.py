def add_contact():
    name = input('Введите имя и фамилию нового контакта (через пробел): ').split()
    if tuple(name) in contact_book:
        print('Такой человек уже есть в контактах.')
        print()
    else:
        phone_number = int(input('Введите номер телефона: '))
        contact_book[tuple(name)] = phone_number
        print('Текущий словарь контактов:', contact_book)
        print()


def find_human():
    surname = input('Введите фамилию для поиска: ')
    for i_key in contact_book.keys():
        if surname in i_key:
            print(i_key[0], i_key[1], contact_book[i_key])
            print()


contact_book = dict()
while True:
    print('Введите номер действия: ')
    action = int(input(' 1. Добавить контакт \n 2. Найти человека \n'))
    if action == 1:
        add_contact()
    elif action == 2:
        find_human()
    else:
        print('Ошибка ввода. Введите 1 или 2')
