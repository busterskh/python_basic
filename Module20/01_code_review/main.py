def interests(dict):
    interests = set([
                     j
                     for i_dict in dict
                     for j in dict[i_dict]['interests']
    ])
    return interests


def long_surname(dict):
    string = ''
    for i in dict:
        string += dict[i]['surname']
    long = len(string)

    return long


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

pairs = [(i, students[i]['age']) for i in students]

print('Список пар "ID студента — возраст": {0}'.format(pairs))
print('Полный список интересов всех студентов: {0} '
      '\nОбщая длина всех фамилий студентов: {1}'.format(interests(students), long_surname(students)))
