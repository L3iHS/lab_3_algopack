from src.sorts.bubble_sort import bubble_sort


def bucket_sort(arr: list[float], buckets: int | None = None) -> list[float]:
    
    if len(arr) <= 1:
        return arr.copy()
    
    a = arr.copy()

    if buckets is None:
        buckets = len(a)
    elif not isinstance(buckets, int) or buckets < 1:
        raise TypeError('buckets должен быть целым числом >= 1')
    
    min_value = a[0]
    max_value = a[0]
    for x in a:
        if not isinstance(x, (float, int)):
            raise TypeError('bucket_sort принимает только числа')
        if x < min_value:
            min_value = x
        if x > max_value:
            max_value = x


    bucket_count = buckets  # если будет два числа, веозбмется первое
    bucket_lists: list[list] = [[] for _ in range(bucket_count)]

    if max_value == min_value:
        return a
    
    for x in a:
        # x - min_value чтобы сделать все числа от 0 до 1
        index = int( (x - min_value) / (max_value - min_value) * (bucket_count - 1))
        bucket_lists[index].append(x)

    result = []
    for bucket in bucket_lists:
        result.extend(bubble_sort(bucket))
    
    return result