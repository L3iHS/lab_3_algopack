def bubble_sort(arr: list[int]) -> list[int]:
    a = arr.copy()
    n = len(a)

    # (n - 1) так как последний индекс который будем брать для сравнения
    for i in range(n - 1):
        swapped = False
        # так же n - 1 и еще -уже отсортированное (- i)
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    
    return a