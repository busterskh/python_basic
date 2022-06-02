import collections
import zipfile


def unzip(arhive):
    zfile = zipfile.ZipFile(arhive, 'r')
    for file_name in zfile.namelist():
        zfile.extract(file_name)
    zfile.close()


def letter_stats(file_name):
    result = dict()
    if file_name.endswith('.zip'):
        unzip(file_name)
        file_name = ''.join(file_name[:-3] + 'txt')
    file_text = open(file_name, 'r', encoding='utf-8')
    for line in file_text:
        for letter in line:
            if letter.isalpha():
                if letter not in result:
                    result[letter] = 0
                result[letter] += 1
    file_text.close()
    answer(result)


def answer(result):
    frequency = sorted(result.values(), reverse=True)
    letters_dict = collections.OrderedDict()
    for i in frequency:
        for j in result.keys():
            if i == result[j]:
                letters_dict[j] = i

    for key, value in letters_dict.items():
        print(key, value)


file_name = 'voyna-i-mir.zip'
letter_stats(file_name)
