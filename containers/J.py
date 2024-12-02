n = int(input())

for i in range(n):
    a = list(map(float, input().split()))
    
    for i in range(1, len(a) - 2):
        b = False
        if a[i] < a[i + 1] and a[i + 2] < a[i] < a[i + 1]:
            b = True
        if b:
            print(0)
            break
    else:
        print(1)