def create_dict(count_pair):
    synonym_dict = dict()
    for i in range(count_pair):
        print('{0} пара:'.format(i + 1), end=' ')
        pair = input().split(' — ')
        synonym_dict[pair[0]] = pair[1]
        synonym_dict[pair[1]] = pair[0]

    return synonym_dict


def user_qestion(synonim_dict):
    user_word = input('Введите слово: ')
    while user_word.title() not in synonim_dict:
        print('Такого слова в словаре нет.')
        user_word = input('Введите слово: ')
    else:
        print('Синоним: {0}'.format(synonim_dict[user_word.title()]))


count_pair = int(input('Введите количество пар слов: '))

synonym_dict = create_dict(count_pair)

user_qestion(synonym_dict)