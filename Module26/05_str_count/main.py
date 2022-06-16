import os

start_path = os.path.abspath(os.path.join('..', '..', '..', '..'))


def gen_files_path(path, dir_name):
    for way, fold, file_name in os.walk(path):
        if dir_name in str(way):
            return str(way), fold, file_name


def python_file(way):
    string = 0
    for file in os.listdir(way):
        if file.endswith('.py'):
            with open(file, 'r') as py_file:
                for j in py_file:
                    print(j)
                    if j.startswith('#'):
                        pass
                    elif j.isspace():
                        pass
                    else:
                        string += 1
        elif os.path.isdir(file):
            string_in_dir = python_file(file)
            string += string_in_dir
    return string


name = input('Введите директорию: ')
print(start_path)

name_way, folder, file = gen_files_path(start_path, name)
direction = folder + file

total_sting = python_file(name_way)
print('Количество строк в файлах директории: {}'.format(total_sting))
