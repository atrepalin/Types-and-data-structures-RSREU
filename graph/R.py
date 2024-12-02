directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, grid, visited, M, N):
    stack = [(x, y)]
    visited[x][y] = True
    
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                stack.append((nx, ny))

def pieces(M, N, grid):
    visited = [[False] * N for _ in range(M)]
    count = 0

    for i in range(M):
        for j in range(N):
            if grid[i][j] == '#' and not visited[i][j]:
                dfs(i, j, grid, visited, M, N)
                count += 1

    return count

M, N = map(int, input().split())
grid = [input().strip() for _ in range(M)]

print(pieces(M, N, grid))