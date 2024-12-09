N, E = map(int, input().split())
M = int(input())

INF = float("inf")
stops = [[] for _ in range(N + 1)]

for _ in range(M):
    data = list(map(int, input().split()))
    K = data[0]
    prev_station, prev_time = data[1], data[2]

    for i in range(3, 2 * K, 2):
        station, time = data[i], data[i + 1]

        stops[prev_station].append((prev_time, time, station))

        prev_station, prev_time = station, time

dist = [INF] * (N + 1)
dist[1] = 0

visited = [False] * (N + 1)

while True:
    station = -1
    time = INF

    for i in range(1, N + 1):
        if not visited[i] and dist[i] < time:
            time = dist[i]
            station = i

    if time == INF:
        break

    visited[station] = True

    for edge in stops[station]:
        begin, end, dst = edge
        if begin >= dist[station] and end < dist[dst]:
            dist[dst] = end


print(dist[E] if dist[E] != INF else -1)
