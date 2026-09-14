class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.index = 0
    def add(self, item):
        self.buffer[self.index % self.size] = item
        self.index += 1
    def get_all(self):
        return self.buffer