import random
from src.errors import InvalidParameterError


# с помощью seed получаем предскаемую последовательность случайных чисел
# при одинаковом seed будут одинаковые последовательности
def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    """
    Макссив рандомных целых чисел в [lo, hi]
    """

    if n < 0:
        raise InvalidParameterError("n должен быть >= 0")
    if lo > hi:
        raise InvalidParameterError("lo не может быть больше hi")

    rng = random.Random(seed)

    if distinct:
        max_unique = hi - lo + 1
        if n > max_unique:
            raise InvalidParameterError("нельзя сгенерировать n различных чисел в заданном диапазоне")
        values = list(range(lo, hi + 1))
        rng.shuffle(values)
        return values[:n]

    # с повторениями
    return [rng.randint(lo, hi) for _ in range(n)]


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """
    Почти отсортированный массив
    меняем местами случайные элементы заданное число раз
    """
    
    if n < 0:
        raise InvalidParameterError("n должен быть >= 0")
    if swaps < 0:
        raise InvalidParameterError("swaps должен быть >= 0")

    arr = list(range(n))
    rng = random.Random(seed)  # позволяет генерировать одиноковые последовательности

    if n <= 1:
        return arr

    for _ in range(swaps):
        i = rng.randrange(n)
        j = rng.randrange(n)
        if n > 1:
            while j == i:
                j = rng.randrange(n)
        arr[i], arr[j] = arr[j], arr[i]  # меняем местами 2 рандомных элемента

    return arr


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    """
    Массив с большим количеством дубликатов
    """

    if n < 0:
        raise InvalidParameterError("n должен быть >= 0")
    if k_unique < 1:
        raise InvalidParameterError("k_unique должен быть >= 1")

    if n == 0:
        return []

    rng = random.Random(seed)
    unique_values = list(range(k_unique))

    return [rng.choice(unique_values) for _ in range(n)]


def reverse_sorted(n: int) -> list[int]:
    """
    Обратно отсортированный массив
    """

    if n < 0:
        raise InvalidParameterError("n должен быть >= 0")
    return list(range(n - 1, -1, -1))


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    """
    Массив рандомных вещественных чисел  в [lo, hi)
    """
    if n < 0:
        raise InvalidParameterError("n должен быть >= 0")
    if lo > hi:
        raise InvalidParameterError("lo не может быть больше hi")

    rng = random.Random(seed)

    if n == 0:
        return []

    result: list[float] = []
    span = hi - lo

    for _ in range(n):
        value = lo + rng.random() * span  # random() возвращает [0.0, 1.0)
        result.append(value)  # при 0 равно lo, при 1 почти равно hi

    return result