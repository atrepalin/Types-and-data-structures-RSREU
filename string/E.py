def z_func(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    left, right = 0, 0
    for i in range(1, n):
        k = max(0, min(z[i - left], right - i))
        while i + k < n and s[k] == s[i + k]:
            k += 1
        z[i] = k
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


text = input()

p = z_func(text)

print(*p)
