text = input('Введите текст: ')
list_word = list([x for x in text.lower() if x in 'аиеоуыэ'])
print('Список гласных букв:', list_word)
print('Длина списка:', len(list_word))
