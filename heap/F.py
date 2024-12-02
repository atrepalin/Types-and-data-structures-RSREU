import heapq

n = int(input())
arrivals = [tuple(map(int, input().split())) for _ in range(n)]

arrivals.sort()
heap = []
max_machines = 0

for arrival, length in arrivals:
    while heap and heap[0] <= arrival:
        heapq.heappop(heap)
    
    heapq.heappush(heap, arrival + length)
    
    max_machines = max(max_machines, len(heap))

print(max_machines)