from src.errors import NonIntegerArgumentError, NegativeArgumentError


def fibo_2(n: int, memory=None) -> int:
    if not isinstance(n, int):
        raise NonIntegerArgumentError("n должно быть целым числом")
    if n < 0:
        raise NegativeArgumentError('n должно быть не отрицательным')
    if memory is None:
        memory = {0: 0, 1: 1}
    # чтобы не словарь не был общим для всех вызовов
    if n not in memory:
        memory[n] = fibo_2(n - 1, memory) + fibo_2(n - 2, memory)
    return memory[n]