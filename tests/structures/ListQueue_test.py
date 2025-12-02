import pytest
from src.structures.queue import ListQueue
from src.errors import QueueEmptyError


def test_empty_queue():
    q = ListQueue()
    assert q.is_empty()
    assert len(q) == 0

    with pytest.raises(QueueEmptyError):
        q.dequeue()

    with pytest.raises(QueueEmptyError):
        q.front()


def test_enqueue_dequeue_order_and_len():
    q = ListQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert not q.is_empty()
    assert len(q) == 3
    assert q.front() == 1

    assert q.dequeue() == 1
    assert len(q) == 2
    assert q.front() == 2

    assert q.dequeue() == 2
    assert len(q) == 1
    assert q.front() == 3

    assert q.dequeue() == 3
    assert q.is_empty()
    assert len(q) == 0

    with pytest.raises(IndexError):
        q.dequeue()
    with pytest.raises(IndexError):
        q.front()


def test_mixed_operations():
    q = ListQueue()
    q.enqueue(10)
    q.enqueue(20)
    assert q.front() == 10

    assert q.dequeue() == 10
    q.enqueue(30)
    q.enqueue(40)

    # [20, 30, 40]
    assert q.front() == 20
    assert q.dequeue() == 20
    assert q.dequeue() == 30
    assert q.dequeue() == 40
    assert q.is_empty()