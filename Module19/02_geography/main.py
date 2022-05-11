country_dict = dict()
count_country = int(input('Количество стран: '))

for i_county in range(count_country):
    print('{0} страна: '.format(i_county + 1), end='')
    country_and_sity = input().split()
    country_dict[country_and_sity[0]] = country_and_sity[1:]

for i_sity in range(3):
    print('{0} город:'.format(i_sity + 1), end=' ')
    sity = input()
    flag = False
    for i in country_dict.keys():
        if sity in country_dict[i][:]:
            print('Город {0} расположен в стране {1}.'.format(sity, i))
            flag = True
            break
    if flag is False:
        print('По городу {0} данных нет.'.format(sity))
