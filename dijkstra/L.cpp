#include <iostream>
#include <vector>
#include <limits>
#include <queue>
#include <climits>

using namespace std;

const long long INF = LLONG_MIN;

struct Edge
{
    int from, to, weight, index;
};

int main()
{
    int n, m, k;
    cin >> n >> m >> k;

    vector<Edge> edges(m);
    vector<int> concerts(k);

    for (int i = 0; i < m; ++i)
    {
        cin >> edges[i].from >> edges[i].to >> edges[i].weight;
        edges[i].from--;
        edges[i].to--;
        edges[i].index = i + 1;
    }

    for (int i = 0; i < k; ++i)
    {
        cin >> concerts[i];
        concerts[i]--;
    }

    vector<vector<long long>> dp(n, vector<long long>(n, INF));
    vector<vector<int>> next_city(n, vector<int>(n, -1));

    for (int i = 0; i < n; ++i)
        dp[i][i] = 0;

    for (const auto &edge : edges)
    {
        if (dp[edge.from][edge.to] < edge.weight)
        {
            dp[edge.from][edge.to] = edge.weight;
            next_city[edge.from][edge.to] = edge.index;
        }
    }

    for (int via = 0; via < n; ++via)
    {
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (dp[i][via] != INF && dp[via][j] != INF)
                {
                    if (dp[i][j] < dp[i][via] + dp[via][j])
                    {
                        dp[i][j] = dp[i][via] + dp[via][j];
                        next_city[i][j] = next_city[i][via];
                    }
                }
            }
        }
    }

    for (int i = 0; i < n; ++i)
    {
        if (dp[i][i] > 0)
        {
            vector<bool> reachable(n, false);
            for (int j = 0; j < n; ++j)
            {
                if (dp[i][j] != INF && dp[j][i] != INF)
                {
                    reachable[j] = true;
                }
            }
            for (int city : concerts)
            {
                if (reachable[city])
                {
                    cout << "infinitely kind" << endl;
                    return 0;
                }
            }
        }
    }

    vector<int> path;
    for (int i = 0; i < k - 1; ++i)
    {
        int start = concerts[i];
        int end = concerts[i + 1];

        if (dp[start][end] == INF)
        {
            cout << "infinitely kind" << endl;
            return 0;
        }

        int u = start;
        while (u != end)
        {
            path.push_back(next_city[u][end]);
            u = edges[next_city[u][end] - 1].to;
        }
    }

    cout << path.size() << endl;
    for (int idx : path)
    {
        cout << idx << " ";
    }
    cout << endl;

    return 0;
}