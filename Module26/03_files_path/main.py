import os

start_path = os.path.abspath(os.path.join('..', '..', '..', '..'))


def gen_files_path(path, dir_name):
    for way, fold, file_name in os.walk(path):
        if dir_name in str(way):
            return str(way), fold, file_name


name = input('Введите директорию: ')
print(start_path)
name_way, folder, file = gen_files_path(start_path, name)
direction = folder + file
for i in direction:
    print(os.path.join(name_way, i))
