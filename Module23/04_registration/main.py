def input_data():
    with open('registrations.txt', 'r', encoding='utf-8') as registration_data:
        for line in registration_data:
            data = line.split()
            check_result = check_data(line, data)
            if check_result:
                with open('registrations_good.log', 'a') as good_log:
                    good_log.write(line)


def check_data(line, data):
    with open('registrations_bad.log', 'a') as bad_log:
        try:
            if len(data) != 3:
                raise IndexError
            elif not data[0].isalpha():
                raise NameError
            elif '@' and '.' not in data[1]:
                raise SyntaxError
            elif 10 > int(data[2]) > 99:
                raise ValueError
        except IndexError:
            bad_log.write(line[:-1] + '\t\tНЕ присутствуют все три поля\n')
        except NameError:
            bad_log.write(line[:-1] + '\t\tПоле «Имя» содержит НЕ только буквы\n')
        except SyntaxError:
            bad_log.write(line[:-1] + '\t\tПоле «Имейл» НЕ содержит @ и . (точку)\n')
        except ValueError:
            bad_log.write(line[:-1] + '\t\tПоле «Возраст» НЕ является числом от 10 до 99:\n')
        else:
            return True


def print_result():
    with open('registrations_bad.log', 'r') as bad_log:
        info_bad = bad_log.read()
        print(f'Содержимое файла registrations_bad.log:\n {info_bad}')

    with open('registrations_good.log', 'r') as good_log:
        info_good = good_log.read()
        print(f'Содержимое файла registrations_good.log:\n{info_good}')


input_data()
print_result()
