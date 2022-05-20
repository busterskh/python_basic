import os


def check_exists(folder_way):
    if os.path.exists(folder_way):
        check_directory(folder_way)
        print('Размер каталога (в Кб): {0} \n'
              'Количество подкаталогов: {1} \n'
              'Количество файлов: {2}'.format(result['total_size'], result['count_folder'], result['count_file'])
              )
    else:
        print('Такого каталога не существует.')


def check_directory(directory):
    if os.path.isdir(directory):
        for element in os.listdir(directory):
            if os.path.isdir(os.path.join(directory, element)):
                result['count_folder'] += 1
                element_folder = os.path.join(directory, element)
                check_directory(element_folder)
            else:
                result['count_file'] += 1
                result['total_size'] += os.stat(os.path.join(directory, element)).st_size / 1024


result = {'total_size': 0,
          'count_folder': 0,
          'count_file': 0
          }
folder_way = input('Введите путь к папке: ')
check_exists(folder_way)
