import pytest
from src.fact_fibo.factorial_recursive import factorial_recursive
from src.errors import NonIntegerArgumentError, NegativeArgumentError


def test_factorial_recursive_basic():
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(5) == 120
    assert factorial_recursive(6) == 720


def test_factorial_recursive_errors():
    with pytest.raises(NegativeArgumentError):
        factorial_recursive(-10)
    with pytest.raises(NonIntegerArgumentError):
        factorial_recursive(2.7)