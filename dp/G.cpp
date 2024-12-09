#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> dp(n + 1, INT_MAX);
    vector<pair<int, int>> prev(n + 1, {-1, -1});
    dp[1] = 0;

    queue<int> q;
    q.push(1);

    while (!q.empty())
    {
        int current = q.front();
        q.pop();

        vector<pair<int, int>> next_numbers = {
            {current + 1, 1},
            {current * 2, 2},
            {current * 3, 3}};

        for (const auto &[next_num, operation] : next_numbers)
        {
            if (next_num <= n && dp[next_num] > dp[current] + 1)
            {
                dp[next_num] = dp[current] + 1;
                prev[next_num] = {current, operation};
                q.push(next_num);
            }
        }
    }

    vector<int> operations;
    while (n != 1)
    {
        auto [parent, op] = prev[n];
        operations.push_back(op);
        n = parent;
    }

    reverse(operations.begin(), operations.end());
    for (int op : operations)
    {
        cout << op;
    }
    cout << endl;

    return 0;
}
