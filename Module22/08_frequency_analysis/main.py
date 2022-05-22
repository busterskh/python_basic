def count_letter(text):
    all_letters = 0
    for letter in text.lower():
        if letter.isalpha() and letter in letters:
            letters[letter] += 1
            all_letters += 1

        elif letter.isalpha() and letter not in letters:
            letters[letter] = 1
            all_letters += 1
    frequency_analysis(all_letters)


def frequency_analysis(all_letters):
    frequency = sorted(letters.values(), reverse=True)
    letters_dict = dict()
    for i in frequency:
        for j in sorted(letters.keys()):
            if i == letters[j]:
                letters_dict[j] = i

    with open('analysis.txt', 'a') as outcoming_file:
        for letter, count in letters_dict.items():
            letters_dict[letter] /= all_letters
            outcoming_file.write(f'{letter} {str(letters_dict[letter])[:5]}\n')
    outcoming_file.close()

    with open('analysis.txt', 'r') as output_file:
        text = output_file.read()
        print(f'Содержимое файла analysis.txt:\n{text}')


with open('text.txt', 'r') as incoming_text:
    file_text = incoming_text.read()
    print(f'Содержимое файла text.txt:\n{file_text}')
incoming_text.close()
letters = dict()
count_letter(file_text)
