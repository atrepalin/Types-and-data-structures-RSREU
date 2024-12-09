from collections import deque


def is_inside(x, y, N):
    return 1 <= x <= N and 1 <= y <= N


def bfs(N, start, end):
    knight_moves = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
    ]

    queue = deque([(start[0], start[1], 0)])

    parent = {start: None}

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == end:
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return steps, path

        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if is_inside(nx, ny, N) and (nx, ny) not in parent:
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny, steps + 1))

    return -1, []


N = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

min_steps, path = bfs(N, (x1, y1), (x2, y2))

print(min_steps)
for x, y in path:
    print(x, y)
