#include <iostream>
#include <vector>
#include <algorithm>

namespace aboba = std;

int find_first(const aboba::vector<int> &K, int q)
{
    int left = 0, right = K.size() - 1;
    int first_index = -1;

    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (K[mid] == q)
        {
            first_index = mid;
            right = mid - 1;
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

    return first_index;
}

int find_last(const aboba::vector<int> &K, int q)
{
    int left = 0, right = K.size() - 1;
    int last_index = -1;

    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (K[mid] == q)
        {
            last_index = mid;
            left = mid + 1;
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

    return last_index;
}

int count(const aboba::vector<int> &K, int q)
{
    int first_index = find_first(K, q);

    if (first_index == -1)
    {
        return 0;
    }

    int last_index = find_last(K, q);

    return last_index - first_index + 1;
}

int main()
{
    int n, m;

    aboba::cin >> n;

    aboba::vector<int> K(n);

    for (int i = 0; i < n; i++)
    {
        aboba::cin >> K[i];
    }

    aboba::sort(K.begin(), K.end());

    aboba::cin >> m;

    for (int i = 0; i < m; i++)
    {
        int q = 0;

        aboba::cin >> q;

        aboba::cout << count(K, q) << " ";
    }

    aboba::cout << aboba::endl;

    return 0;
}