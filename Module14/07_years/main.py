def year_check(year):
    count = 0
    for num in str(year):
        number = num
        for y in str(year):
            if y == number:
                count += 1
        if count >= 3:
            print(year)
            count = 0
            break
        else:
            count = 0


def passed_years(year_start, year_stop):
    print('Года от', year_start, 'до', year_stop, 'с тремя одинаковыми цифрами:')
    for year in range(year_start, year_stop + 1):
        year_check(year)


year_start = int(input('Введите первый год: '))
year_stop = int(input('Введите второй год: '))
passed_years(year_start, year_stop)
