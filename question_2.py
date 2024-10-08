"""
Представлено две реализации циклического буфера FIFO: на основе списка и
на основе двусторонней очереди.
В реализации на основе списка необходимо контролировать большее количество
вещей: положение головы, хвоста и размер буфера. Это же дает большую гибкость.
Например, можно поменять поведение при переполении. Или немного модифицировать
метод .get() и обеспечить доступ к элементам буфера по индексу за O(1).
В то же время, если размер буфера значительно превышает количество текущих
лементов, большая часть памяти может использоваться впустую.
Реализация на основе deque проще для понимания и более читабельна, меньше
возможностей для ошибка: необходимые операции поддерживаются из коробки.
Но, соответственно, обладает меньшей гибкостью.
В целом, выполнение стандартных операций будет и там, и там за O(1).
"""
from collections import deque


class CircularBufferList:
    def __init__(self, size=10):
        """Инициализация буфера на основе списка.
        Если размер буфера не указан - используется значение 10."""
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0

    def append(self, item):
        """Вставка элемента в конец буфера."""
        self.buffer[self.tail] = item
        if self.is_full():
            self.head = (self.head + 1) % self.size
        else:
            self.count += 1
        self.tail = (self.tail + 1) % self.size

    def get(self):
        """Вернуть головной элемент буфера."""
        return self.buffer[self.head]

    def pop(self):
        """Вернуть и удалить головной элемент из буфера."""
        if self.is_empty():
            raise IndexError("Буфер пустой: невозможно удалить элемент.")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return item

    def is_empty(self):
        """Вернуть True, если буфер пустой."""
        return self.count == 0

    def is_full(self):
        """Вернуть True, если буфер полный."""
        return self.count == self.size

    def __str__(self):
        """Строковое представление буфера."""
        return str([item for item in self.buffer])


class CircularBufferDeque:
    def __init__(self, size=10):
        """Инициализация буфера на основе двусторонней очереди.
        Если размер буфера не указан - используется значение 10."""
        self.size = size
        self.buffer = deque(maxlen=size)

    def append(self, item):
        """Вставка элемента в конец буфера."""
        self.buffer.append(item)

    def get(self):
        """Вернуть головной элемент буфера."""
        return self.buffer[0]

    def pop(self):
        """Вернуть и удалить головной элемент из буфера."""
        return self.buffer.popleft()

    def __str__(self):
        """Строковое представление буфера."""
        return str([item for item in self.buffer])
