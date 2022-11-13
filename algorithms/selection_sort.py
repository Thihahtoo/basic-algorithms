def find_max_index(items):
    max_i = 0
    max = items[max_i]
    for i in range(len(items)):
        if items[i] > max:
            max = items[i]
            max_i = i
    return max_i

def find_min_index(items):
    min_i = 0
    min = items[min_i]
    for i in range(len(items)):
        if items[i] < min:
            min = items[i]
            min_i = i
    return min_i


def sort(items, order = 'desc'):
    sorted = []
    if order == 'desc':
        for i in range(len(items)):
            index = find_max_index(items)
            sorted.append(items[index])
            items.pop(index)
    elif order == 'asc':
        for i in range(len(items)):
            index = find_min_index(items)
            sorted.append(items[index])
            items.pop(index)
    return sorted