class Trie:
    def __init__(self): self.root = {}
    def add(self, w):
        n = self.root
        for c in w: n = n.setdefault(c, {})
        n["$"] = True
    def starts(self, p):
        n = self.root
        for c in p:
            if c not in n: return []
            n = n[c]
        out = []
        def dfs(n, path):
            for k, v in n.items():
                if k == "$": out.append(p + path)
                else: dfs(v, path + k)
        dfs(n, "")
        return out

t = Trie()
for w in ["code", "coder", "cod", "cat", "dog"]: t.add(w)
print(t.starts("co"))