n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

matrix = [[False] * n for _ in range(n)]

for u, v in edges:
    matrix[u - 1][v - 1] = True
    matrix[v - 1][u - 1] = True

for i in range(n):
    for j in range(i + 1, n):
        if not matrix[i][j]:
            print("NO")
            exit()

print("YES")