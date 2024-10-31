class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity <0:
            raise ValueError
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n < 0 or self.size + n > self.capacity:
            raise ValueError
        self.size += n


    def withdraw(self, n):
        if n > self.size or n < 0:
            raise ValueError
        self.size -= n

    @property
    def get_capacity(self):
        return self.capacity
    @property
    def get_size(self):
        return self.size

