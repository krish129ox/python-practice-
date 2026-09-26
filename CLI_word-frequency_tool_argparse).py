import argparse
from collections import Counter

p = argparse.ArgumentParser(description="Top words in a file")
p.add_argument("file")
p.add_argument("-n", type=int, default=5)
a = p.parse_args()
print(Counter(open(a.file).read().lower().split()).most_common(a.n))
# run: python tool.py notes.txt -n 10