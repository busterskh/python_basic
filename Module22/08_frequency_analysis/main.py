def count_letter(text):
    all_letters = 0
    for letter in text.lower():
        if letter.isalpha() and letter in letters:
            letters[letter] += 1

        elif letter.isalpha() and letter not in letters:
            letters[letter] = 1
            all_letters += 1
    frequency_analysis(all_letters)


def frequency_analysis(all_letters):
    outcoming_file = open('analysis.txt', 'a')

    for letter, count in sorted(letters.items()):
        letters[letter] = all_letters / 100 * count
        outcoming_file.write(f'{letter} {str(letters[letter])}\n')


incoming_text = open('text.txt', 'r')
file_text = incoming_text.read()
incoming_text.close()
letters = dict()
count_letter(file_text)
