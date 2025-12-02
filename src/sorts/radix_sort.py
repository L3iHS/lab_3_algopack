from src.errors import NonIntegerArgumentError, NegativeArgumentError, InvalidParameterError


def radix_sort(arr: list[int], base: int = 10) -> list[int]:
    """
    Работает только с неотрицательными числами
    """
    if len(arr) <= 1:
        return arr.copy()
    
    if not isinstance(base, int) or base < 2:
        raise InvalidParameterError("base должен быть целым числом >= 2")

    a = arr.copy()

    max_value = a[0]
    for x in a:
        if not isinstance(x, int):
            raise NonIntegerArgumentError('"radix_sort принимает только целые числа"')
        if x < 0:
            raise NegativeArgumentError('radix_sort работает только с неотрицательными числами')
        if x > max_value:
            max_value = x
    
    exp = 1
    while exp <= max_value:
        buckets = [[] for _ in range(base)]
        for x in a:
            digit = (x // exp) % base
            buckets[digit].append(x)

        new_a = []
        for d in range(base):
            new_a.extend(buckets[d])
        
        a = new_a
        exp *= base
    
    return a