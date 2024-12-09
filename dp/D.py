n, M = map(int, input().split())
m = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [0] * (M + 1)
selected = [[False] * (M + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(M, m[i - 1] - 1, -1):
        if dp[j - m[i - 1]] + c[i - 1] > dp[j]:
            dp[j] = dp[j - m[i - 1]] + c[i - 1]
            selected[i][j] = True

result = []
w = M
for i in range(n, 0, -1):
    if selected[i][w]:
        result.append(i)
        w -= m[i - 1]

print(*result, sep="\n")
