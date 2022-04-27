def create_dict(text):
    word_dict = dict()

    for i_word in text:
        if i_word in word_dict:
            word_dict[i_word] += 1
        else:
            word_dict[i_word] = 1

    print('Оригинальный словарь частот:')
    for i_key in word_dict.keys():
        print(i_key, ':', word_dict[i_key])

    return word_dict


def invertional_dict(word_dict):
    new_word_dict = dict()

    for i_item in word_dict.keys():
        if word_dict[i_item] in new_word_dict:
            new_word_dict[word_dict[i_item]].append(i_item)
        else:
            new_word_dict[word_dict[i_item]] = list(i_item)

    print('\nИнвертированный словарь частот:')
    for i_key in new_word_dict.keys():
        print(i_key, ':', new_word_dict[i_key])


text = input('Введите текст: ')

word_dict = create_dict(text)

invertional_dict(word_dict)

