def max_significance(n, a):
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]

    max_significance = 0
    best_l = 0
    best_r = 0

    stack = []
    
    for i in range(n):
        while stack and a[stack[-1]] >= a[i]:
            j = stack.pop()
            left_bound = stack[-1] if stack else -1
            current_sum = prefix_sum[i] - prefix_sum[left_bound + 1]
            current_significance = current_sum * a[j]
            if current_significance > max_significance:
                max_significance = current_significance
                best_l = left_bound + 1
                best_r = i - 1
        
        stack.append(i)

    while stack:
        j = stack.pop()
        left_bound = stack[-1] if stack else -1
        current_sum = prefix_sum[n] - prefix_sum[left_bound + 1]
        current_significance = current_sum * a[j]
        if current_significance > max_significance:
            max_significance = current_significance
            best_l = left_bound + 1
            best_r = n - 1

    return max_significance, best_l + 1, best_r + 1

n = int(input().strip())
a = list(map(int, input().strip().split()))

significance, *days = max_significance(n, a)
print(significance)
print(*days)