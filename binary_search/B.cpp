#include <iostream>
#include <vector>
#include <algorithm>

namespace aboba = std;

int search(const aboba::vector<int> &K, int q)
{
    int left = 0;
    int right = K.size() - 1;
    int ind = -1;

    while (left <= right)
    {
        int mid = left + (right - left) / 2;

        if (ind == -1 || abs(K[mid] - q) < abs(K[ind] - q) ||
            (abs(K[mid] - q) == abs(K[ind] - q) && K[mid] < K[ind]))
        {
            ind = mid;
        }

        if (K[mid] < q)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }

    return K[ind];
}

int main()
{
    int n, k;

    aboba::cin >> n >> k;

    aboba::vector<int> K(n);

    for (int i = 0; i < n; ++i)
    {
        aboba::cin >> K[i];
    }

    aboba::sort(K.begin(), K.end());

    for (int i = 0; i < k; ++i)
    {
        int q;

        aboba::cin >> q;

        aboba::cout << search(K, q) << aboba::endl;
    }

    return 0;
}