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


current = input().strip()
target = input().strip()

s = current + "#" + target
pi = prefix(s)

print(len(current) - pi[-1])
