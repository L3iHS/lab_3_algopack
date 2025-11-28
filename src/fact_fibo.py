def factorial(n: int) -> int:
    if n < 0:
        raise ValueError('n должно быть не отрицательным')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError('n должно быть не отрицательным')
    if n <= 1:  # на всякий, чтобы не ушел в рекурсию
        return 1
    return factorial_recursive(n - 1) * n


def fibo_1(n: int) -> int:
    if n < 0:
        raise ValueError('n должно быть не отрицательным')
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# print(fibo_1(1))
# print(fibo_1(2))
# print(fibo_1(3))

def fibo_2(n: int, memory=None) -> int:
    if n < 0:
        raise ValueError('n должно быть не отрицательным')
    if memory is None:
        memory = {0: 0, 1: 1}
    # чтобы не словарь не был общим для всех вызовов
    if n not in memory:
        memory[n] = fibo_2(n - 1, memory) + fibo_2(n - 2, memory)
    return memory[n]

# print(fibo_2(1))
# print(fibo_2(2))
# print(fibo_2(3))

# from functools import lru_cache
# @lru_cache(maxsize=None)
# def fib_2(n):
#     if n < 2:
#         return n
#     return fib_2(n - 1) + fib_2(n - 2)
# или как в егэ, но тут нужен импорт

def fibo_recursive(n: int) -> int:
    if n < 0:
        raise ValueError('n должно быть не отрицательным')
    if n <= 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)