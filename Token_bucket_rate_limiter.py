import time

class Bucket:
    def __init__(self, rate, cap):
        self.rate, self.cap = rate, cap
        self.tokens, self.t = cap, time.monotonic()
    def allow(self):
        now = time.monotonic()
        self.tokens = min(self.cap, self.tokens + (now - self.t) * self.rate)
        self.t = now
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False

b = Bucket(rate=2, cap=3)
print([b.allow() for _ in range(5)])  # [True, True, True, False, False]