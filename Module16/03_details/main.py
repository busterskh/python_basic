shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

what_count = input('Название товара: ')

summ = 0
count = 0
for i in range(len(shop)):
    if shop[i][0] == what_count.casefold():
        count += 1
        summ += shop[i][1]

print('Кол-во деталей -', count)
print('Общая стоимость -', summ)
