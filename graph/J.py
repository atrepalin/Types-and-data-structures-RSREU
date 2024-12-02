n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
permutation = list(map(int, input().split()))

position = {vertex: i for i, vertex in enumerate(permutation)}
    
for u, v in edges:
    if position[u] >= position[v]:
        print("NO")
        exit()

print("YES")