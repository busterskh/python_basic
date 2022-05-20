import os


def directory_way(text):
    directory = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split()
    file_name = input('Введите имя файла:') + '.txt'
    file_way = ''
    for folder in directory:
        file_way = os.path.join(file_way, folder)
    file_way = os.path.join(file_way, file_name)
    if os.path.exists(file_name):
        file = open(file_way, 'w')
        re_write = input('Вы действительно хотите перезаписать файл? ')
        if re_write.lower() == 'да':
            file.write(text)
            print('Файл успешно перезаписан!')
            file.close()
        else:
            print('Отмена перезаписи.')
    else:
        file = open(file_way, 'w')
        file.write(text)
        print('Файл успешно сохранён! ')
        file.close()
    # else:
    #     print('Недействительный путь')


user_text = input('Введите строку: ')

directory_way(user_text)
