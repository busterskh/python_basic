def family(surname):
    for i in family_dict:
        if surname in i or surname + 'а' in i:
            print(i[0], i[1], family_dict[i])


family_dict = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Петров', 'Женя'): 24,
    ('Петров', 'Ваня'): 26,
    ('Петров', 'Рома'): 22,
    ('Иванова', 'Катя'): 27,
    ('Иванов', 'Ваня'): 29
}

surname = input('Введите фамилию: ').title()
print()
family(surname)