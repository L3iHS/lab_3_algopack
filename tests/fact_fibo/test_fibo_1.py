import pytest
from src.fact_fibo import fibo_1


def test_fibo_1_basic_sequence():
    assert fibo_1(0) == 0
    assert fibo_1(1) == 1
    assert fibo_1(2) == 1
    assert fibo_1(3) == 2
    assert fibo_1(4) == 3
    assert fibo_1(5) == 5
    assert fibo_1(6) == 8
    assert fibo_1(7) == 13


def test_fibo_1_errors():
    with pytest.raises(ValueError):
        fibo_1(-1)
    with pytest.raises(TypeError):
        fibo_1(1.5)