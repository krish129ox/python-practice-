import random
from collections import defaultdict

text = "the cat sat on the mat and the dog sat on the log".split()
model = defaultdict(list)
for a, b in zip(text, text[1:]): model[a].append(b)

w = random.choice(text); out = [w]
for _ in range(12):
    w = random.choice(model[w]) if model[w] else random.choice(text)
    out.append(w)
print(" ".join(out))