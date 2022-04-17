text = input('Введите строку: ')
longest_word = max(text.split(), key=len)

print('Самое длинное слово:', longest_word)
print('Длина этого слова:', len(longest_word))