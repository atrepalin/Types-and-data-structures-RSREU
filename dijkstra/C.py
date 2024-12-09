import heapq


def dijkstra_with_path(graph, start, end, n):
    distances = [float("inf")] * n
    distances[start] = 0
    predecessors = [-1] * n
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in range(n):
            weight = graph[current_vertex][neighbor]
            if weight == -1:
                continue

            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    if distances[end] == float("inf"):
        return -1

    path = []
    current = end
    while current != -1:
        path.append(current + 1)
        current = predecessors[current]

    return path[::-1]


N, S, F = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

S -= 1
F -= 1

result = dijkstra_with_path(graph, S, F, N)

if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))
