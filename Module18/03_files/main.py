special_sym = '@№$%^&\*()'
name_file = input('Название файла: ')

for i in special_sym:
    if not name_file.endswith('.txt' or '.docx'):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
        break
    else:
        if name_file.startswith(i):
            print('Ошибка: название начинается на один из специальных символов.')
            break
        else:
            print('Файл назван верно.')
            break
