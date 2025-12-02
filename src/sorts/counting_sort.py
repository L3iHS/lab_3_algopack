from src.errors import NonIntegerArgumentError


def counting_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr.copy()
    a = arr.copy()
    min_value = a[0]
    max_value = a[0]
    for x in a:
        if not isinstance(x, int):
            raise NonIntegerArgumentError('counting_sort принимает только целые значения')
        if x < min_value:
            min_value = x
        if x > max_value:
            max_value = x

    size = max_value - min_value + 1
    counts = [0] * size

    for x in a:
        # сдвигаем на -min_value, чтобы не было проблем с отрицательными числами
        index = x - min_value
        counts[index] += 1

    result = []
    for i in range(len(counts)):
        value = min_value + i
        result.extend([value] * counts[i])

    return result
