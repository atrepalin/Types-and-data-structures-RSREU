import heapq


def guppy_fish_birth_time(n, populations):
    events = []

    for i in range(n):
        f = populations[i]
        wait_time = max(1000 - f, 1)
        birth_time = wait_time
        heapq.heappush(events, (birth_time, i))

    current_time = 0
    current_position = 0
    while events:
        birth_time, aquarium_index = heapq.heappop(events)

        travel_time = abs(current_position - aquarium_index)
        time_available = birth_time - current_time

        if travel_time > time_available:
            return birth_time

        current_time = birth_time
        current_position = aquarium_index

        populations[aquarium_index] += 1
        new_f = populations[aquarium_index]
        wait_time = max(1000 - new_f, 1)
        new_birth_time = current_time + wait_time
        heapq.heappush(events, (new_birth_time, aquarium_index))


n = int(input())
populations = [int(input()) for _ in range(n)]

result = guppy_fish_birth_time(n, populations)
print(result)
