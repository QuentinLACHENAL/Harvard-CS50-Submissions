class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._n = 0

    def __str__(self):
        return "🍪" * self._n

    def deposit(self, n):
        self._n += n
        if self._n > self._capacity:
            raise ValueError

    def withdraw(self, n):
        self._n -= n
        if self._n < 0:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    @property
    def size(self):
        return self._n

    @size.setter
    def size(self, value):
        self._size = value



