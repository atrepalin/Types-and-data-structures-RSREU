#include <iostream>
#include <vector>
#include <algorithm>
bool canPlaceCows(const std::vector<int> &stalls, int k, int min_dist)
{
    int count = 1;
    int last_position = stalls[0];

    for (int i = 1; i < stalls.size(); i++)
    {
        if (stalls[i] - last_position >= min_dist)
        {
            count++;
            last_position = stalls[i];
            if (count == k)
            {
                return true;
            }
        }
    }
    return false;
}

int main()
{
    int n, k;
    std::cin >> n >> k;
    std::vector<int> stalls(n);

    for (int i = 0; i < n; i++)
    {
        std::cin >> stalls[i];
    }

    std::sort(stalls.begin(), stalls.end());

    int left = 1;
    int right = stalls[n - 1] - stalls[0];

    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (canPlaceCows(stalls, k, mid))
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }

    std::cout << right << std::endl;

    return 0;
}