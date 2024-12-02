#include <iostream>
#include <vector>
#include <algorithm>

namespace aboba = std;

bool canCut(const aboba::vector<long long> &ropes, long long length, int K)
{
    int count = 0;
    for (long long rope : ropes)
    {
        count += rope / length;
        if (count >= K)
            return true;
    }
    return count >= K;
}

int main()
{
    int N, K;
    aboba::cin >> N >> K;

    aboba::vector<long long> ropes(N);
    for (int i = 0; i < N; ++i)
    {
        aboba::cin >> ropes[i];
    }

    long long left = 1, right = *max_element(ropes.begin(), ropes.end()), result = 0;

    while (left <= right)
    {
        long long mid = (left + right) / 2;

        if (canCut(ropes, mid, K))
        {
            result = mid;
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }

    aboba::cout << result << aboba::endl;
    return 0;
}