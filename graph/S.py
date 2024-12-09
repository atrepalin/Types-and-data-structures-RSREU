from collections import deque

moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]


def chess_to_index(chess_pos):
    column, row = chess_pos
    return ord(column) - ord("a"), int(row) - 1


def bfs(start_x, start_y):
    board = [[-1] * 8 for _ in range(8)]
    queue = deque([(start_x, start_y)])
    board[start_x][start_y] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == -1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))

    return board


def min_moves(pos1, pos2):
    start1_x, start1_y = chess_to_index(pos1)
    start2_x, start2_y = chess_to_index(pos2)

    board1 = bfs(start1_x, start1_y)
    board2 = bfs(start2_x, start2_y)

    min_moves = float("inf")

    for i in range(8):
        for j in range(8):
            if board1[i][j] != -1 and board2[i][j] != -1:
                if board1[i][j] == board2[i][j]:
                    min_moves = min(min_moves, board1[i][j])

    return min_moves if min_moves != float("inf") else -1


pos1, pos2 = input().split()

print(min_moves(pos1, pos2))
