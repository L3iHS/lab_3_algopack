def quick_sort(arr: list[int]) -> list[int]:
    # pivot - разделяющий элемент
    a = arr.copy()

    if len(a) <= 1:
        return a
    
    pivot = a[len(a) // 2]
    left = []
    middle = []
    right = []

    for x in a:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)

