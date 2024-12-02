#include <iostream>
#include <algorithm>

namespace aboba = std;

bool canMakeCopies(long long time, int N, int x, int y)
{
    return (time / x) + (time / y) >= N;
}

int main()
{
    int N, x, y;
    aboba::cin >> N >> x >> y;

    if (x > y)
        aboba::swap(x, y);

    long long left = 0, right = static_cast<long long>(N) * x;

    while (left <= right)
    {
        long long mid = (left + right) / 2;

        if (canMakeCopies(mid, N - 1, x, y))
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }

    aboba::cout << left + x << aboba::endl;

    return 0;
}