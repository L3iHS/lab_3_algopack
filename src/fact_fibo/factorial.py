from src.errors import NonIntegerArgumentError, NegativeArgumentError


def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise NonIntegerArgumentError("n должно быть целым числом")
    if n < 0:
        raise NegativeArgumentError('n должно быть не отрицательным')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
