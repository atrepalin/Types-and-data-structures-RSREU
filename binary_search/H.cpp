#include <iostream>

namespace aboba = std;

bool canPlace(long x, long w, long h, long n)
{
    return (x / w) * (x / h) >= n;
}

int main()
{
    long w, h, n;

    aboba::cin >> w >> h >> n;

    long left = 0, right = aboba::max(w, h) * n;

    while (right - left > 1)
    {
        long mid = (left + right) / 2;

        if (canPlace(mid, w, h, n))
            right = mid;
        else
            left = mid;
    }

    aboba::cout << right << aboba::endl;
}