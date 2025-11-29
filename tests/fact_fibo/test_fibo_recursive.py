import pytest
from src.fact_fibo import fibo_recursive


def test_fibo_recursive_shifted_sequence():
    assert fibo_recursive(0) == 1
    assert fibo_recursive(1) == 1
    assert fibo_recursive(2) == 2
    assert fibo_recursive(3) == 3
    assert fibo_recursive(4) == 5
    assert fibo_recursive(5) == 8


def test_fibo_recursive_errors():
    with pytest.raises(ValueError):
        fibo_recursive(-1)
    with pytest.raises(TypeError):
        fibo_recursive(2.5)