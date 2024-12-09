def floyd(N, dist):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


N, M = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]

inf = float("inf")
dist = [[inf] * N for _ in range(N)]

for i in range(N):
    dist[i][i] = 0

for s, e, l in roads:
    dist[s - 1][e - 1] = l
    dist[e - 1][s - 1] = l

floyd(N, dist)

max_distances = []

for i in range(N):
    max_distances.append(max(dist[i]))

best_building = min(range(N), key=lambda i: (max_distances[i], i))

print(best_building + 1)
