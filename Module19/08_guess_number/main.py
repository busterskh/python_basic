max_number = int(input('Введите максимальное число: '))
numbers_list = set([i for i in range(1, max_number + 1)])
potencial_number = ''

while True:
    potencial_number = input('\nНужное число есть среди вот этих чисел: ')
    if potencial_number != 'Помогите!':
        potencial_number = potencial_number.split(' ')
        answer_Artem = input('Ответ Артёма: ')
        if answer_Artem.lower() == 'да':
            numbers_list = set(potencial_number)
        elif answer_Artem.lower() == 'нет':
            numbers_list = numbers_list.difference(set(potencial_number))
        else:
            print('Ошибка! Артем ответил что-то непонятное. Повторите вопрос.')
    else:
        print("Артём мог загадать следующие числа: ", ', '.join(list(numbers_list)))
        break
