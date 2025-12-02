import pytest
from src.fact_fibo.factorial import factorial
from src.errors import NonIntegerArgumentError, NegativeArgumentError


def test_factorial_basic():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(6) == 720


def test_factorial_errors():
    with pytest.raises(NegativeArgumentError):
        factorial(-1)
    with pytest.raises(NonIntegerArgumentError):
        factorial(3.5)
    with pytest.raises(NonIntegerArgumentError):
        factorial("10")