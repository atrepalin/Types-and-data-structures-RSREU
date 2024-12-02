#include <iostream>
#include <vector>
#include <algorithm>

namespace aboba = std;

bool search(const aboba::vector<int> &K, int q)
{
    int left = 0;
    int right = K.size() - 1;

    while (left <= right)
    {
        int mid = (left + right) / 2;

        if (K[mid] == q)
        {
            return true;
        }
        else if (K[mid] < q)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }

    return false;
}

int main()
{
    int n, k;
    aboba::cin >> n >> k;

    aboba::vector<int> K(n);
    for (int i = 0; i < n; i++)
    {
        aboba::cin >> K[i];
    }

    aboba::sort(K.begin(), K.end());

    for (int i = 0; i < k; i++)
    {
        int q = 0;

        aboba::cin >> q;

        aboba::cout << (search(K, q) ? "YES" : "NO") << aboba::endl;
    }
}