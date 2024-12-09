def floyd(N, s, t, adjacency_matrix):
    inf = float("inf")
    dist = [
        [
            inf if adjacency_matrix[i][j] == -1 else adjacency_matrix[i][j]
            for j in range(N)
        ]
        for i in range(N)
    ]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] < inf and dist[k][j] < inf:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    result = dist[s - 1][t - 1]
    return -1 if result == inf else result


N, s, t = map(int, input().split())
adjacency_matrix = [list(map(int, input().split())) for _ in range(N)]

result = floyd(N, s, t, adjacency_matrix)
print(result)
