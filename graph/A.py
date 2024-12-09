n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if matrix[i][i] == 1:
        print("NO")
        exit()
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            print("NO")
            exit()

print("YES")
