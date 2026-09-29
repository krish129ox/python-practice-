class Positive:
    def __set_name__(self, owner, name): self.n = "_" + name
    def __get__(self, obj, t=None): return getattr(obj, self.n)
    def __set__(self, obj, v):
        if v <= 0: raise ValueError("must be positive")
        setattr(obj, self.n, v)

class Item:
    price = Positive()
    def __init__(self, price): self.price = price

print(Item(10).price)
Item(-5)  # ValueError