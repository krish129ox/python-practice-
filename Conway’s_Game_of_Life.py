from collections import Counter

def step(live):
    c = Counter((x + dx, y + dy) for x, y in live
                for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0))
    return {p for p, n in c.items() if n == 3 or (n == 2 and p in live)}

g = {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)}  # glider
for _ in range(4): g = step(g)
print(sorted(g))