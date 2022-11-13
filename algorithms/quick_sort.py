def quick_sort(l):
    if len(l) > 1:
        pivot = l[0]
        low = []
        high = []
        for i in l[1:]:
            if i <= pivot:
                low.append(i)
            else:
                high.append(i)
        return (quick_sort(low) + [pivot] + quick_sort(high))
    else:
        return l