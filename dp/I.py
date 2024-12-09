n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]

dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + times[i - 1][0]
    
    if i > 1:
        dp[i] = min(dp[i], dp[i - 2] + times[i - 2][1])
        
    if i > 2:
        dp[i] = min(dp[i], dp[i - 3] + times[i - 3][2])

print(dp[n])
