from src.errors import NonIntegerArgumentError, NegativeArgumentError


def fibo_recursive(n: int) -> int:
    if not isinstance(n, int):
        raise NonIntegerArgumentError("n должно быть целым числом")
    if n < 0:
        raise NegativeArgumentError('n должно быть не отрицательным')
    if n <= 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)