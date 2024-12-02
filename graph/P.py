from collections import deque

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start, end = (0, 0), (rows - 1, cols - 1)

    if matrix[start[0]][start[1]] == -1 \
        or matrix[end[0]][end[1]] == -1:
        return -1

    queue = deque([(start, 0)])

    visited = set()
    visited.add(start)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        current, distance = queue.popleft()

        if current == end:
            return distance

        for direction in directions:
            next_cell = (current[0] + direction[0], current[1] + direction[1])

            if 0 <= next_cell[0] < rows and \
                0 <= next_cell[1] < cols and \
                matrix[next_cell[0]][next_cell[1]] == 0 and \
                next_cell not in visited:
                queue.append((next_cell, distance + 1))

                visited.add(next_cell)
    return -1

n, m = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

result = shortest_path(matrix)
print(result)