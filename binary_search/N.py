def can_chop(D, A, K, B, M, X):
    F = D - D // K
    S = D - D // M
    return X <= F * A + S * B


A, K, B, M, X = map(int, input().split())

left = 0
right = X // min(A, B) + 1

while left <= right:
    mid = (left + right) // 2

    if not can_chop(mid, A, K, B, M, X):
        left = mid + 1
    else:
        right = mid - 1

print(left)
