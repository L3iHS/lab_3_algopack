import pytest
from src.structures.stack import ListStack
from src.errors import StackEmptyError


def test_empty_stack():
    s = ListStack()
    assert s.is_empty()
    assert len(s) == 0

    with pytest.raises(StackEmptyError):
        s.pop()

    with pytest.raises(StackEmptyError):
        s.peek()

    with pytest.raises(StackEmptyError):
        s.min()


def test_push_pop_order_and_len():
    s = ListStack()
    s.push(1)
    s.push(2)
    s.push(3)

    assert not s.is_empty()
    assert len(s) == 3
    assert s.peek() == 3

    assert s.pop() == 3
    assert len(s) == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()
    assert len(s) == 0


def test_min_behavior():
    s = ListStack()
    s.push(3)
    assert s.min() == 3

    s.push(5)
    assert s.min() == 3 

    s.push(2)
    assert s.min() == 2

    s.push(2)
    assert s.min() == 2

    s.push(4)
    assert s.min() == 2

    assert s.pop() == 4
    assert s.min() == 2

    assert s.pop() == 2
    assert s.min() == 2

    assert s.pop() == 2
    assert s.min() == 3

    assert s.pop() == 5
    assert s.min() == 3

    assert s.pop() == 3
    assert s.is_empty()