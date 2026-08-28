import csv
def count_rows(filename):
    with open(filename) as f:
        return sum(1 for _ in csv.reader(f))