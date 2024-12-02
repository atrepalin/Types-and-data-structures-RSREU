def prefix(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p

text = input()

s = input()

p = prefix(s + '#' + text)

for i in range(len(s) + 1, len(s) + len(text) + 1):
    if p[i] == len(s):
        print(i - 2 * len(s), end=' ')

print()