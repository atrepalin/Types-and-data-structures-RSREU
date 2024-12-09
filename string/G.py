text = input()

modified_text = "#" + "#".join(text) + "#"
n = len(modified_text)
p = [0] * n
center = 0
right = 0
total_palindromes = 0

for i in range(n):
    mirror = 2 * center - i

    if i < right:
        p[i] = min(right - i, p[mirror])

    while (
        i + p[i] + 1 < n
        and i - p[i] - 1 >= 0
        and modified_text[i + p[i] + 1] == modified_text[i - p[i] - 1]
    ):
        p[i] += 1

    if i + p[i] > right:
        center = i
        right = i + p[i]

    total_palindromes += (p[i] + 1) // 2

print(total_palindromes)
