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

if s == text:
    print(0)
    exit()

if len(text) != len(s):
    print(-1)
    exit()

doubled = text + text

p = prefix(s + '#' + doubled)
for i in range(len(s) + 1, len(doubled) + len(s) + 1):
    if p[i] == len(s):
        print(len(s) - (i - 2 * len(s)))
        exit()

print(-1)