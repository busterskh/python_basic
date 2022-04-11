text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
rus_alphabet = list('абвгдежзиклмнопрстуфхцчшщъыьэюя')
cipher_text = [rus_alphabet[rus_alphabet.index(i_text) + shift - len(rus_alphabet)]
               if i_text in rus_alphabet
               else i_text
               for i_text in text]

cipher_massage = ''
for i in cipher_text:
    cipher_massage += i
# for i_text in text:
#     if i_text in alphabet:
#         if alphabet.index(i_text) + 3 > len(alphabet):
#             cipher_text += alphabet[alphabet.index(i_text) + 3]
#         else:
#             cipher_text += alphabet[alphabet.index(i_text) + 3 - len(alphabet)]
#     else:
#         cipher_text += i_text
print('Зашифрованное сообщение:', cipher_massage)
