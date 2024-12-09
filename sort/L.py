distances = list(map(int, input().split()))
rates = list(map(int, input().split()))

distances.sort(reverse=True)
rates.sort()

cost = sum(d * r for d, r in zip(distances, rates))
print(cost)
