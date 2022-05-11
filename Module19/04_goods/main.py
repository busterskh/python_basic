goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


goods_summ = dict()
for i_goods in goods:
    goods_summ[i_goods] = {'quantity' : 0,'price': 0}
    if goods[i_goods] in store:
        for j_goods in range(len(store[goods[i_goods]])):
            goods_summ[i_goods]['quantity'] += store[goods[i_goods]][j_goods]['quantity']
            goods_summ[i_goods]['price'] += store[goods[i_goods]][j_goods]['quantity'] * store[goods[i_goods]][j_goods]['price']

for i_key in goods_summ:
    print('{0} — {1} штук, стоимость {2} рубля'.format(i_key, goods_summ[i_key]['quantity'], goods_summ[i_key]['price']))