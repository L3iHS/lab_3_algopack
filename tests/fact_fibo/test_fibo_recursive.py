import pytest
from src.fact_fibo.fibo_recursive import fibo_recursive
from src.errors import NonIntegerArgumentError, NegativeArgumentError

def test_fibo_recursive_shifted_sequence():
    assert fibo_recursive(0) == 1
    assert fibo_recursive(1) == 1
    assert fibo_recursive(2) == 2
    assert fibo_recursive(3) == 3
    assert fibo_recursive(4) == 5
    assert fibo_recursive(5) == 8


def test_fibo_recursive_errors():
    with pytest.raises(NegativeArgumentError):
        fibo_recursive(-1)
    with pytest.raises(NonIntegerArgumentError):
        fibo_recursive(2.5)