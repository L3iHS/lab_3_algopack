import pytest
from src.fact_fibo import factorial_recursive


def test_factorial_recursive_basic():
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(5) == 120
    assert factorial_recursive(6) == 720


def test_factorial_recursive_errors():
    with pytest.raises(ValueError):
        factorial_recursive(-10)
    with pytest.raises(TypeError):
        factorial_recursive(2.7)