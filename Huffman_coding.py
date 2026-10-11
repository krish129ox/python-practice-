import heapq
from collections import Counter

def huffman(s):
    h = [[w, [c, ""]] for c, w in Counter(s).items()]
    heapq.heapify(h)
    while len(h) > 1:
        lo, hi = heapq.heappop(h), heapq.heappop(h)
        for p in lo[1:]: p[1] = "0" + p[1]
        for p in hi[1:]: p[1] = "1" + p[1]
        heapq.heappush(h, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return dict(h[0][1:])

print(huffman("abracadabra"))