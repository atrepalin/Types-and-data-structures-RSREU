def floyd(N, adjacency_matrix):
    inf = float('inf')
    dist = [row[:] for row in adjacency_matrix]
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] != inf and dist[k][j] != inf:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    for i in range(N):
        if dist[i][i] < 0:
            return -1

    min_distance = inf
    for i in range(N):
        for j in range(N):
            if i != j:
                min_distance = min(min_distance, dist[i][j])
    
    return min_distance

N = int(input())
adjacency_matrix = [list(map(int, input().split())) for _ in range(N)]

result = floyd(N, adjacency_matrix)
print(result)