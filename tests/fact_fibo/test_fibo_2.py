import pytest
from src.fact_fibo.fibo_1 import fibo_1
from src.fact_fibo.fibo_2 import fibo_2
from src.errors import NegativeArgumentError, NonIntegerArgumentError


def test_fibo_2_same_as_fibo_1():
    for n in range(0, 10):
        assert fibo_2(n) == fibo_1(n)


def test_fibo_2_errors():
    with pytest.raises(NegativeArgumentError):
        fibo_2(-5)
    with pytest.raises(NonIntegerArgumentError):
        fibo_2("3") 