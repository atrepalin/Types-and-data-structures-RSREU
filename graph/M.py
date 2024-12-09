from collections import defaultdict, deque


def is_bipartite(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * (n + 1)

    def bfs(start):
        queue = deque([start])
        color[start] = 1
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if color[v] == 0:
                    color[v] = -color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
        return True

    for i in range(1, n + 1):
        if color[i] == 0:
            if not bfs(i):
                return "NO", []

    first_table = [i for i in range(1, n + 1) if color[i] == 1]
    return "YES", first_table


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

result, first_table = is_bipartite(n, edges)

if result == "YES":
    print("YES")
    print(" ".join(map(str, first_table)))
else:
    print("NO")
