PRIME = 31
MOD = 10**9 + 7


def prime_power(n):
    p = [1] * (n + 1)

    for i in range(1, n + 1):
        p[i] = (p[i - 1] * PRIME) % MOD

    return p


def hash_func(s):
    hashes = [0] * (len(s) + 1)

    for i in range(len(s)):
        hashes[i + 1] = (hashes[i] * PRIME + (ord(s[i]) - ord("a") + 1)) % MOD

    return hashes


def get_hash(p, hashes, l, r):
    return (hashes[r] - hashes[l - 1] * p[r - l + 1]) % MOD


text = input()

s = input()

hashes = hash_func(text)
p = prime_power(len(hashes) - 1)

pattern = hash_func(s)[-1]

for i in range(len(text) - len(s) + 2):
    if get_hash(p, hashes, i, i + len(s) - 1) == pattern:
        print(i - 1, end=" ")

print()
