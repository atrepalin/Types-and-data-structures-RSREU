from collections import deque

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def in_bounds(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


def bfs(N, M, maze):
    start = (0, 0)

    queue = deque([(start[0], start[1], 0)])

    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while queue:
        x, y, moves = queue.popleft()

        if maze[x][y] == 2:
            return moves

        for dx, dy in directions:
            nx, ny = x, y

            while in_bounds(nx + dx, ny + dy, N, M) and maze[nx + dx][ny + dy] != 1:
                nx += dx
                ny += dy

                if maze[nx][ny] == 2:
                    return moves + 1

            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))

    return -1


N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

print(bfs(N, M, maze))
