import heapq
from collections import defaultdict

def dijkstra(N, d, v, R, routes):
    graph = defaultdict(list)
    for route in routes:
        start, departure, end, arrival = route
        graph[start].append((end, departure, arrival))
    
    min_time = [float('inf')] * (N + 1)
    min_time[d] = 0
    
    pq = [(0, d)]
    
    while pq:
        curr_time, curr_village = heapq.heappop(pq)
        
        if curr_village == v:
            return curr_time
        
        if curr_time > min_time[curr_village]:
            continue
        
        for next_village, departure, arrival in graph[curr_village]:
            if departure >= curr_time:
                new_time = arrival
                if new_time < min_time[next_village]:
                    min_time[next_village] = new_time
                    heapq.heappush(pq, (new_time, next_village))
    
    return -1

N = int(input())
d, v = map(int, input().split()) 
R = int(input())

buses = []
for _ in range(R):
    buses.append(list(map(int, input().split())))

print(dijkstra(N, d, v, R, buses))