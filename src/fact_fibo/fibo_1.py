from src.errors import NonIntegerArgumentError, NegativeArgumentError


def fibo_1(n: int) -> int:
    if not isinstance(n, int):
        raise NonIntegerArgumentError("n должно быть целым числом")
    if n < 0:
        raise NegativeArgumentError('n должно быть не отрицательным')
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a