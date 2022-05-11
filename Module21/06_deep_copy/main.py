def change_model(model):
    site = {
        'html': {
            'head': {
                'title': f'Куплю/продам {model} недорого'
            },
            'body': {
                'h2': f'У нас самая низкая цена на {model}',
                'div': 'Купить',
                'p': 'продать'
            }
        }
    }
    print('site = ')
    answer(site)


def answer(site):
    for i_key in site.keys():
        if isinstance(site[i_key], dict):
            print(f'\t{i_key}: ', end='\n\t')
            answer(site[i_key])
        else:
            print(f'\t\t{i_key}: {site[i_key]}', end='\n\t')


count_site = int(input('Сколько сайтов: '))

for i_name in range(count_site):
    model_name = input('\nВведите название продукта для нового сайта: ')
    print(f'Сайт для {model_name}:')
    change_model(model_name)



