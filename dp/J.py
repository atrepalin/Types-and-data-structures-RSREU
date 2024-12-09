n, m = map(int, input().split())

for i in range(1, 96):
    a = int((1 + 5**0.5) / 2 * i + 1)
    b = int((3 + 5**0.5) / 2 * i + 1)

    if (n == a and m == b) or (n == b and m == a):
        print(2)
        break
else:
    print(1)
