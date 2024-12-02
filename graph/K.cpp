#include <iostream>
#include <vector>

using namespace std;

void dfs(int v, const vector<vector<int>> &graph, vector<int> &tin, vector<int> &tout, int &timer)
{
    tin[v] = timer++;
    for (int u : graph[v])
    {
        if (tin[u] == -1)
        {
            dfs(u, graph, tin, tout, timer);
        }
    }
    tout[v] = timer++;
}

void preprocess_tree(int n, const vector<int> &parents, vector<int> &tin, vector<int> &tout)
{
    vector<vector<int>> graph(n + 1);
    int root = 0;

    for (int i = 1; i <= n; ++i)
    {
        int p = parents[i - 1];
        if (p == 0)
        {
            root = i;
        }
        else
        {
            graph[p].push_back(i);
        }
    }

    int timer = 0;
    dfs(root, graph, tin, tout, timer);
}

bool is_ancestor(const vector<int> &tin, const vector<int> &tout, int a, int b)
{
    return tin[a] <= tin[b] && tout[a] >= tout[b];
}

int main()
{
    int n, m;
    cin >> n;

    vector<int> parents(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> parents[i];
    }

    cin >> m;
    vector<pair<int, int>> queries(m);
    for (int i = 0; i < m; ++i)
    {
        cin >> queries[i].first >> queries[i].second;
    }

    vector<int> tin(n + 1, -1), tout(n + 1, -1);
    preprocess_tree(n, parents, tin, tout);

    for (const auto &[a, b] : queries)
    {
        if (is_ancestor(tin, tout, a, b))
        {
            cout << "1\n";
        }
        else
        {
            cout << "0\n";
        }
    }

    return 0;
}