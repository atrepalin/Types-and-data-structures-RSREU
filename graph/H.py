def dijkstra(matrix, start):
    n = len(matrix)
    used = [False] * n
    dist = [float("inf")] * n
    path = [[] for _ in range(n)]
    dist[start] = 0

    for _ in range(n):
        min_dist = float("inf")
        min_dist_index = -1
        for i in range(n):
            if not used[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_dist_index = i

        used[min_dist_index] = True

        for i in range(n):
            if not used[i] and matrix[min_dist_index][i] != 0:
                new_dist = dist[min_dist_index] + matrix[min_dist_index][i]
                if new_dist < dist[i]:
                    dist[i] = new_dist
                    path[i] = path[min_dist_index] + [min_dist_index]

    return dist, path


n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

a, b = map(int, input().split())

dist, path = dijkstra(matrix, a - 1)

dst = dist[b - 1]

if dst == float("inf"):
    print(-1)
    exit()

print(dist[b - 1])

if dst != 0:
    print(*([a] + path[b - 1][:-1] + [b]))
