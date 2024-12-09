C = float(input())

left = 0.0
right = C

while right - left > 1e-7:
    mid = (left + right) / 2
    f_mid = mid**2 + mid**0.5 - C

    if f_mid < 0:
        left = mid
    else:
        right = mid

print(f"{((left + right) / 2):.6f}")
