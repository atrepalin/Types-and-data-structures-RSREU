def count_connected(n, s, matrix):
    start_vertex = s - 1

    visited = [False] * n

    def dfs(v):
        visited[v] = True
        for u in range(n):
            if matrix[v][u] == 1 and not visited[u]:
                dfs(u)

    dfs(start_vertex)

    return sum(visited)


n, s = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(count_connected(n, s, matrix))
