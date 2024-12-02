def has_cycle(matrix):
    n = len(matrix)
    visited = [0] * n

    def dfs(v):
        if visited[v] == 1:
            return True
        if visited[v] == 2:
            return False
        
        visited[v] = 1
        
        for u in range(n):
            if matrix[v][u] == 1:
                if dfs(u):
                    return True
        
        visited[v] = 2
        return False
    
    for i in range(n):
        if visited[i] == 0:
            if dfs(i):
                return 1
            
    return 0

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(has_cycle(matrix))