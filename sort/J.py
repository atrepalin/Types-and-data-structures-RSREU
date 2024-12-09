from functools import cmp_to_key
from sys import stdin

parts = []

for line in stdin:
    parts.append(line.strip())


def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1


parts.sort(key=cmp_to_key(compare))

print("".join(parts))
