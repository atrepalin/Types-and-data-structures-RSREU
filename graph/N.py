def dfs(v, graph, count):
    graph[v][1] = 1
    for next in graph[v][0]:
        if graph[next][1] == 0:
            dfs(next, graph, count)
        elif graph[next][1] == 1:
            count[0] += 1
    graph[v][1] = 2


n = int(input())
graph = [[[], 0] for _ in range(n)]

for i in range(n):
    key = int(input())
    graph[key - 1][0].append(i)

count = [0]
for i in range(n):
    if graph[i][1] == 0:
        dfs(i, graph, count)

print(count[0])
