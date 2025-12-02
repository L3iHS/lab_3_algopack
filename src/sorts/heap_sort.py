def heap_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr.copy()
    
    a = arr.copy()

    for x in a:
        if not isinstance(x, int):
            raise TypeError('heap_sort принимает только целые значения')

    n = len(a)


    def heapify(a: list[int], heap_size: int, i: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
                
        if left < heap_size and a[left] > a[largest]:
            largest = left

        if right < heap_size and a[right] > a[largest]:
            largest = right

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(a, heap_size, largest)


    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        heapify(a, end, 0)
    
    return a