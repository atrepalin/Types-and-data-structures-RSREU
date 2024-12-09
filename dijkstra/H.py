def floyd(N, adjacency_matrix):
    closure = [row[:] for row in adjacency_matrix]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    return closure


N = int(input())
adjacency_matrix = [list(map(int, input().split())) for _ in range(N)]

closure = floyd(N, adjacency_matrix)

for row in closure:
    print(" ".join(map(str, row)))
