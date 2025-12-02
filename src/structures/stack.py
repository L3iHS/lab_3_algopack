from __future__ import annotations
from src.errors import StackEmptyError

class ListStack:
    def __init__(self) -> None:
        self._data: list[int] = []
        self._mins: list[int] = []

    def push(self, x: int) -> None:
        self._data.append(x)
        if not self._mins or x <= self._mins[-1]:
            self._mins.append(x)

    def pop(self) -> int:
        if self.is_empty():
            raise StackEmptyError("Стек пуст")
        val = self._data.pop()
        if val == self._mins[-1]:
            self._mins.pop()
            # проблемы с разностью в длинах не будет, так как
            # первый элемент стека всегда будет первым в списке минимумов
        return val

    def peek(self) -> int:
        if self.is_empty():
            raise StackEmptyError("Стек пуст")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def min(self) -> int:
        if self.is_empty():
            raise StackEmptyError("Стек пуст")
        return self._mins[-1]


class LinkedListStack:
    class _Node:
        def __init__(self, value: int, next: LinkedListStack._Node | None = None, current_min: int | None = None) -> None:
            self.value = value
            self.next = next  # сслыка на элемент до (ниже в стеке)
            self.current_min = current_min  # локальный минимум

    def __init__(self) -> None:
        self._head: LinkedListStack._Node | None = None  # последний элемент стека
        self._size: int = 0
    
    def is_empty(self) -> bool:
        return self._head is None
    
    def __len__(self) -> int:
        return self._size
    
    def push(self, x: int) -> None:
        if self.is_empty():
            new_node = self._Node(x, None, x)
        else:
            current_min = min(x, self._head.current_min)
            new_node = self._Node(x, self._head, current_min)
        self._head = new_node
        self._size += 1
    
    def pop(self) -> int:
        if self.is_empty():
            raise StackEmptyError('Стек пуст')
        val = self._head.value
        self._head = self._head.next
        self._size -= 1
        return val
    
    def peek(self) -> int:
        if self.is_empty():
            raise StackEmptyError('Стек пуст')
        return self._head.value
    
    def min(self) -> int:
        if self.is_empty():
            raise StackEmptyError('Стек пуст')
        return self._head.current_min
