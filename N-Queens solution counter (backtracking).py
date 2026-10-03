def queens(n):
    def solve(r, cols, d1, d2):
        if r == n: return 1
        total = 0
        for c in range(n):
            if c in cols or r - c in d1 or r + c in d2: continue
            total += solve(r + 1, cols | {c}, d1 | {r - c}, d2 | {r + c})
        return total
    return solve(0, frozenset(), frozenset(), frozenset())

print(queens(8))  # 92