site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search(construct, key, deep):
    if isinstance(deep, int):
        if deep < 1:
            return None
        deep -= 1

    if key in construct:
        return construct[key]

    for i_construct in construct.values():
        if isinstance(i_construct, dict):
            result = search(i_construct, key, deep)
            if result:
                break
    else:
        result = None

    return result


searching_key = input('Введите искомый ключ: ')
max_deep = input('Хотите ввести максимальную глубину? Y/N: ').upper()
if max_deep == 'Y':
    deep_level = int(input('Введите максимальную глубину: '))
    value = search(site, searching_key, deep_level)
else:
    value = search(site, searching_key, deep=None)

if value:
    print('Значение ключа:', value)
else:
    print('Такого ключа в структуре нет или достигнута заданная глубина.')
