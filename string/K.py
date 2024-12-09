INF = float("inf")

s = input()
t = input()


def calculate_distances(string):
    distances = []
    char_positions = {}

    for i, char in enumerate(string):
        if char not in char_positions:
            distances.append(INF)
        else:
            distances.append(i - char_positions[char])
        char_positions[char] = i

    return distances


dist_t = calculate_distances(t)
dist_s = calculate_distances(s)
dist = dist_t + [-1] + dist_s

n = len(dist)
z = [0] * n
left, right = 0, 0

for i in range(1, n):
    k = max(0, min(z[i - left], right - i))

    while i + k < n and (
        dist[k] == dist[i + k] or dist[k] == INF and i + k - dist[i + k] < i
    ):
        k += 1

    z[i] = k

    if i + z[i] > right:
        left, right = i, i + z[i]

matches = [i - len(t) for i in range(len(t) + 1, n) if z[i] == len(t)]

print(len(matches))
print(*matches)
