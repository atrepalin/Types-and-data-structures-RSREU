from collections import deque

N, K = map(int, input().split())
nums = list(map(int, input().split()))

d = deque()
for i in range(K):
    while d and nums[d[-1]] > nums[i]:
        d.pop()
    d.append(i)

for i in range(K, N):
    print(nums[d[0]])
    while d and nums[d[-1]] > nums[i]:
        d.pop()
    while d and d[0] <= i - K:
        d.popleft()
    d.append(i)

print(nums[d[0]])
