import heapq


def dijkstra(N, costs, roads):
    distances = [float("inf")] * N
    distances[0] = 0

    adjacency_list = [[] for _ in range(N)]

    for road in roads:
        u, v = road
        adjacency_list[u - 1].append(v - 1)
        adjacency_list[v - 1].append(u - 1)

    priority_queue = [(0, 0)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for v in adjacency_list[current_vertex]:
            new_cost = current_distance + costs[current_vertex]

            if new_cost < distances[v]:
                distances[v] = new_cost
                heapq.heappush(priority_queue, (new_cost, v))

    return distances[-1] if distances[-1] != float("inf") else -1


N = int(input())
costs = list(map(int, input().split()))
M = int(input())

roads = []
for _ in range(M):
    u, v = map(int, input().split())
    roads.append((u, v))

print(dijkstra(N, costs, roads))
