def can_order_trains(n, train):
    stack = []
    expected = 1

    for wagon in train:
        while stack and stack[-1] == expected:
            stack.pop()
            expected += 1

        stack.append(wagon)

        while stack and stack[-1] == expected:
            stack.pop()
            expected += 1

    while stack and stack[-1] == expected:
        stack.pop()
        expected += 1

    return expected - 1 == n


n = int(input())
train = list(map(int, input().split()))


if can_order_trains(n, train):
    print("YES")
else:
    print("NO")
