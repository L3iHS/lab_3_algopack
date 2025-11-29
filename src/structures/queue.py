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
            raise IndexError('Очередь пуста')
        return self._data.pop(0)
    
    def front(self) -> int:
        if self.is_empty():
            raise IndexError('Очередь пуста')
        return self._data[0]
    


class LinkedListQueue:
    pass