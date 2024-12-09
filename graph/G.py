def is_tree(n, m, edges):
    if m != n - 1:
        return "NO"

    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)

    def dfs(v):
        stack = [v]
        visited[v] = True
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

    dfs(1)

    if all(visited[1:]):
        return "YES"
    else:
        return "NO"


n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

print(is_tree(n, m, edges))
