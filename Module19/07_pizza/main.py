def create_dict(count):
    orders_dict = dict()
    for i_order in range(count):
        print('{0} заказ:'.format(i_order + 1), end=' ')
        order_info = input().split(' ')
        if order_info[0] not in orders_dict.keys():
            orders_dict[order_info[0]] = {order_info[1] : order_info[2]}
        else:
            if order_info[1] in orders_dict[order_info[0]].keys():
                orders_dict[order_info[0]][order_info[1]] += order_info[2]
            else:
                orders_dict[order_info[0]][order_info[1]] = order_info[2]

    return orders_dict


def print_out(order_dict):
    print()
    for i_key in order_dict.keys():
        print('{0}:'.format(i_key))
        for j_key in order_dict[i_key].keys():
            print('\t{0}: {1}'.format(j_key, order_dict[i_key][j_key]))


count_orders = int(input('Введите количество заказов: '))
order_dict = create_dict(count_orders)
print_out(order_dict)
