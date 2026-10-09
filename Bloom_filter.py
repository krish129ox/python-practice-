import hashlib

class Bloom:
    def __init__(self, m=1024, k=3):
        self.m, self.k, self.bits = m, k, 0
    def _idx(self, x):
        return [int(hashlib.md5(f"{i}{x}".encode()).hexdigest(), 16) % self.m
                for i in range(self.k)]
    def add(self, x):
        for i in self._idx(x): self.bits |= 1 << i
    def __contains__(self, x):
        return all(self.bits >> i & 1 for i in self._idx(x))

b = Bloom()
b.add("krish")
print("krish" in b, "bob" in b)  # True, (almost certainly) False