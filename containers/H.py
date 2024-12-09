from collections import deque

n = int(input())

left = deque()
right = deque()

for _ in range(n):
    i = input().split()

    if i[0] == "+":
        right.append(i[1])
    elif i[0] == "-":
        print(left.popleft())
    else:
        right.appendleft(i[1])

    if len(left) < len(right):
        left.append(right.popleft())
