from __future__ import annotations
from src.errors import QueueEmptyError


class ListQueue:
    def __init__(self):
        self._data: list[int] = []
    
    def is_empty(self) -> bool:
        return len(self._data) == 0
    
    def __len__(self) -> int:
        return len(self._data)
    
    def enqueue(self, x: int) -> None:
        self._data.append(x)
    
    def dequeue(self) -> int:
        if self.is_empty():
            raise QueueEmptyError('Очередь пуста')
        return self._data.pop(0)
    
    def front(self) -> int:
        if self.is_empty():
            raise QueueEmptyError('Очередь пуста')
        return self._data[0]
    


class LinkedListQueue:
    class _Node:
        def __init__(self, value: int, next: LinkedListQueue._Node | None = None) -> None:
            self.value = value
            self.next = next
    
    def __init__(self):
        self._head: LinkedListQueue._Node | None = None
        self._tail: LinkedListQueue._Node | None = None
        self._size = 0
    
    def is_empty(self) -> bool:
        return self._head is None
    
    def __len__(self) -> int:
        return self._size
    
    def enqueue(self, x: int) -> None:
        node = self._Node(x)
        if self.is_empty():
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1
    
    def front(self) -> int:
        if self.is_empty():
            raise QueueEmptyError("Очередь пуста")
        return self._head.value
    
    def dequeue(self) -> int:
        if self.is_empty():
            raise QueueEmptyError('Очередь пуста')
        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return value