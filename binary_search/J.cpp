#include <iostream>

namespace aboba = std;

bool canPlace(long long x, long long w, long long h, long long n, long long a, long long b)
{
    return aboba::max((w / (a + 2 * x)) * (h / (b + 2 * x)), (h / (a + 2 * x)) * (w / (b + 2 * x))) >= n;
}

int main()
{
    long long n, a, b, w, h;

    aboba::cin >> n >> a >> b >> w >> h;

    long long left = 0, right = aboba::min(w, h);

    while (right - left > 1)
    {
        long long mid = (left + right) / 2;

        if (canPlace(mid, w, h, n, a, b))
            left = mid;
        else
            right = mid;
    }

    aboba::cout << left << aboba::endl;
}