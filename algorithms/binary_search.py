def search(searchlist, item):

    first = 0
    last = len(searchlist) - 1
    middle = round((first + last) / 2)

    while first <= last:
        if searchlist[middle] == item:
            return middle
        else:
            if searchlist[middle] > item:
                last = middle - 1
                middle = round((first + last) / 2)
            elif searchlist[middle] < item:
                first = middle + 1
                middle = round((first + last) / 2)
    return None