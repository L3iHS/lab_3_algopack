import pytest
from src.structures.queue import LinkedListQueue
from src.errors import QueueEmptyError


def test_empty_queue():
    q = LinkedListQueue()
    assert q.is_empty()
    assert len(q) == 0

    with pytest.raises(QueueEmptyError):
        q.dequeue()

    with pytest.raises(QueueEmptyError):
        q.front()


def test_enqueue_dequeue_order_and_len():
    q = LinkedListQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    assert not q.is_empty()
    assert len(q) == 3
    assert q.front() == 10

    assert q.dequeue() == 10
    assert len(q) == 2
    assert q.front() == 20

    assert q.dequeue() == 20
    assert len(q) == 1
    assert q.front() == 30

    assert q.dequeue() == 30
    assert q.is_empty()
    assert len(q) == 0

    with pytest.raises(IndexError):
        q.dequeue()


def test_mixed_operations():
    q = LinkedListQueue()

    q.enqueue(5)
    q.enqueue(7)
    assert q.front() == 5

    q.enqueue(9)
    assert len(q) == 3

    assert q.dequeue() == 5
    assert q.front() == 7

    q.enqueue(11)
    # 7, 9, 11
    assert q.dequeue() == 7
    assert q.dequeue() == 9
    assert q.dequeue() == 11

    assert q.is_empty()


def test_enqueue_after_emptying():
    q = LinkedListQueue()

    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2

    assert q.is_empty()

    q.enqueue(3)
    assert q.front() == 3
    assert q.dequeue() == 3
    assert q.is_empty()