from src.errors import NonIntegerArgumentError, NegativeArgumentError


def factorial_recursive(n: int) -> int:
    if not isinstance(n, int):
        raise NonIntegerArgumentError("n должно быть целым числом")
    if n < 0:
        raise NegativeArgumentError('n должно быть не отрицательным')
    if n <= 1:  # "<" на всякий, чтобы не ушел в рекурсию
        return 1
    return factorial_recursive(n - 1) * n
