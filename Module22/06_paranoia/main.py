def cipher_info(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = [alphabet[alphabet.index(letter) + shift - len(alphabet)]
                   if letter in alphabet
                   else letter
                   for letter in text.lower()]

    cipher_massage = ''
    for letter in cipher_text:
        cipher_massage += letter

    cipher_file = open('cipher_text.txt', 'a')
    cipher_file.write(cipher_massage.title() + '\n')
    cipher_file.close()


def shift_for_cipher(text):
    shift = 1
    for string in text.split('\n'):
        cipher_info(string, shift)
        shift += 1


massage = open('text.txt', 'r')

shift_for_cipher(massage.read())
massage.close()