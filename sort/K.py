N = int(input())

if N == 1:
    print(1)
    exit()

permutation = [1, 2] + [0] * (N - 2)

for i in range(2, N):
    permutation[i], permutation[i // 2] = permutation[i // 2], i + 1

print(*permutation)