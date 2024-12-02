#include <iostream>
#include <vector>
#include <algorithm>

namespace aboba = std;

bool canDivide(const aboba::vector<long long> &heights, int R, int C, int mid)
{
    int count = 0;
    int n = heights.size();

    for (int i = 0; i + C - 1 < n; ++i)
    {
        if (heights[i + C - 1] - heights[i] <= mid)
        {
            count++;
            i += C - 1;
        }
    }

    return count >= R;
}

int main()
{
    int N, R, C;
    aboba::cin >> N >> R >> C;

    aboba::vector<long long> heights(N);

    for (int i = 0; i < N; i++)
    {
        aboba::cin >> heights[i];
    }

    aboba::sort(heights.begin(), heights.end());

    long long left = 0, right = heights.back() - heights.front();

    while (left <= right)
    {
        long long mid = (right + left) / 2;

        if (canDivide(heights, R, C, mid))
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }

    aboba::cout << left << aboba::endl;

    return 0;
}