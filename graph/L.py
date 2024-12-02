from collections import defaultdict, deque

def build_tree(n, m, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    spanning_tree_edges = []
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue and len(spanning_tree_edges) < n - 1:
            u = queue.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    spanning_tree_edges.append((u, v))
                    queue.append(v)
                    if len(spanning_tree_edges) == n - 1:
                        return

    bfs(1)
    
    return spanning_tree_edges

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

result = build_tree(n, m, edges)

for u, v in result:
    print(u, v)