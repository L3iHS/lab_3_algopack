import pytest
from src.fact_fibo import fibo_1, fibo_2


def test_fibo_2_same_as_fibo_1():
    for n in range(0, 10):
        assert fibo_2(n) == fibo_1(n)


def test_fibo_2_errors():
    with pytest.raises(ValueError):
        fibo_2(-5)
    with pytest.raises(TypeError):
        fibo_2("3") 