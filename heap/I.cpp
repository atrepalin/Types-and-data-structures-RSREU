#include <iostream>
#include <unordered_set>
#include <list>
#include <queue>
#include <limits.h>

namespace aboba = std;

int main()
{
    int n, k, p, count = 0;
    aboba::cin >> n >> k >> p;

    aboba::list<int> entries[n];
    int history[p];
    for (int i = 0; i < p; i++)
    {
        aboba::cin >> history[i];
        entries[--history[i]].push_back(i);
    }

    aboba::unordered_set<int> cars;
    aboba::priority_queue<aboba::pair<int, int>> ids;

    for (int i = 0; i < p; i++)
    {
        int curr = history[i];
        entries[curr].pop_front();

        if (cars.find(curr) == cars.end())
        {
            if (cars.size() >= k)
            {
                cars.erase(ids.top().second);
                ids.pop();
            }
            count++;
            cars.insert(curr);
        }
        if (entries[curr].empty())
            ids.push({INT_MAX, curr});
        else
            ids.push({entries[curr].front(), curr});
    }

    aboba::cout << count << aboba::endl;
    return 0;
}