n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

sources = []
for j in range(n):
    for i in range(n):
        if matrix[i][j] == 1:
            break
    else:
        sources.append(j + 1)

sinks = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            break
    else:
        sinks.append(i + 1)


print(len(sources))
print(*sources, sep='\n')
print(len(sinks))
print(*sinks, sep='\n')