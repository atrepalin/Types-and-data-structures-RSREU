import heapq


def dijkstra(graph, start, end):
    N = len(graph)
    distances = [float("inf")] * N
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in range(N):
            weight = graph[current_vertex][neighbor]
            if weight == -1:
                continue

            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end] if distances[end] != float("inf") else -1


N, S, F = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

S -= 1
F -= 1

print(dijkstra(graph, S, F))
