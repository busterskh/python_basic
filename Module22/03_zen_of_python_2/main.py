import os


def letter_count(words):
    sum_letter = 0
    for word in words:
        if word.isalpha():
            sum_letter += len(word)
        else:
            for letter in word:
                if letter.isalpha():
                    sum_letter += 1
    print(f'Количество букв в файле: {sum_letter}')


def word_count(text):
    words = text.split()
    letter_count(words)
    print(f'Количество слов в файле: {len(words)}')


def string_count(text):
    strings = len(text.split('\n'))
    print(f'Количество строк в файле: {strings}')


def most_rare_letter(text):
    alphabeth = 'abcdefghijklmnopqrstuvwxyz'
    letters_frequency = {letter: text.count(letter) for letter in alphabeth
                         if text.count(letter) != 0}

    for letter, frequency in letters_frequency.items():
        if min(letters_frequency.values()) == frequency:
            print(f'Наиболее редкая буква: {letter}')
            break


zen_text = open(os.path.join('..', '02_zen_of_python', 'zen.txt'), 'r')
text_in_file = zen_text.read()

word_count(text_in_file)
string_count(text_in_file)
most_rare_letter(text_in_file)

zen_text.close()
