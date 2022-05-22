import os

FILE_EXT = 'txt'


def root_path():
    return os.path.abspath(os.sep)


def get_folder_path(folders_list):
    path = root_path()
    for folder in folders_list:
        path = os.path.join(path, folder)

    return path


def get_input():
    text = input('Введите строку: ')
    save_path = input('\nКуда хотите сохранить документ? ' +
                      'Введите последовательность папок (через пробел):\n')
    save_path = save_path.split(' ')
    file_name = input('\nВведите имя файла: ')
    file_name += '.' + FILE_EXT

    return text, save_path, file_name


def main():
    text, save_path_list, file_name = get_input()
    save_path = get_folder_path(save_path_list)

    if not os.path.exists(save_path):
        print('Введенный путь не существует ')
        print(save_path)
        return

    file_path = os.path.join(save_path, file_name)

    overwrite = False
    if os.path.exists(file_path):
        response = input('Вы действительно хотите перезаписать файл? [ДА/нет] ')
        if response is not None and response.lower().strip() == 'да':
            overwrite = True
    else:
        with open(file_path, 'w') as output_file:
            output_file.write(text)
        print('Файл успешно сохранён!')

        with open(file_path, 'r') as read_output_file:
            file_text = read_output_file.read()
            print(f'Содержимое файла: {file_text}')

    if overwrite:
        with open(file_path, 'w') as output_file:
            output_file.write(text)
        print('Файл успешно перезаписан!')


main()
