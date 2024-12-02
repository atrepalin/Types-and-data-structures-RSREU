import heapq

MAX_TIME = 1440
TRUCK_WEIGHT = 3000000
MUG_WEIGHT = 100

def can_transport(k):
    min_weight = TRUCK_WEIGHT + k * MUG_WEIGHT
    
    graph = [[] for _ in range(n + 1)]
    for u, v, time, weight in roads:
        if weight >= min_weight:
            graph[u].append((v, time))
            graph[v].append((u, time))
            
    pq = [(0, 1)]
    times = [float('inf')] * (n + 1)
    times[1] = 0
    while pq:
        current_time, node = heapq.heappop(pq)
        if current_time > times[node]:
            continue
        for neighbor, travel_time in graph[node]:
            new_time = current_time + travel_time
            if new_time < times[neighbor]:
                times[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))
    return times[n] <= MAX_TIME

n, m = map(int, input().split())
roads = []
for _ in range(m):
    u, v, t, w = map(int, input().split())
    roads.append((u, v, t, w))

left, right = 0, 10**7
answer = 0
while left <= right:
    mid = (left + right) // 2
    if can_transport(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)