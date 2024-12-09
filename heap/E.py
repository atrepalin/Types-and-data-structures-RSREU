import heapq

N = int(input())

nums = list(map(int, input().split()))

heapq.heapify(nums)

sm = 0

for i in range(N - 1):
    x = heapq.heappop(nums)
    y = heapq.heappop(nums)

    s = x + y
    sm += s * 0.05

    heapq.heappush(nums, s)

print("{:.2f}".format(sm))
