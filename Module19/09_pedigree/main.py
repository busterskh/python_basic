def create_dict(n):
    p_tree = dict()
    for i in range(1, n):
        print('{0} пара:'.format(i), end=' ')
        line = input()
        child, parent = line.split()
        p_tree[child] = parent
    return p_tree


def genaration(name):
    if name not in p_tree:
        heights[name] = 0
        return 0
    parent = p_tree[name]
    if parent in heights:
        value = heights[parent] + 1
    else:
        value = genaration(
            parent) + 1
    heights[name] = value
    return value


count_pair = int(input('Введите количество человек: '))

p_tree = create_dict(count_pair)

all_man = set(p_tree.keys()) | set(p_tree.values())

# словарь (предок=поколение)
heights = dict()
for name in all_man:
    if name not in heights:
        genaration(name)

print('\n«Высота» каждого члена семьи:')
for name in sorted(heights):
    print(name, heights[name])

