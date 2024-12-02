#include <iostream>
#include <vector>
#include <functional>

using namespace std;

void find(int n, vector<pair<int, int>> &edges)
{
    vector<vector<int>> adjacency_list(n);
    for (auto &[u, v] : edges)
    {
        adjacency_list[u - 1].push_back(v - 1);
        adjacency_list[v - 1].push_back(u - 1);
    }

    vector<bool> visited(n, false);
    vector<vector<int>> components;

    function<void(int, vector<int> &)> dfs;

    dfs = [&](int v, vector<int> &component)
    {
        visited[v] = true;
        component.push_back(v + 1);
        for (int neighbor : adjacency_list[v])
        {
            if (!visited[neighbor])
            {
                dfs(neighbor, component);
            }
        }
    };

    for (int i = 0; i < n; ++i)
    {
        if (!visited[i])
        {
            vector<int> component;
            dfs(i, component);
            components.push_back(component);
        }
    }

    cout << components.size() << endl;
    for (auto &component : components)
    {
        cout << component.size() << endl;
        for (int v : component)
        {
            cout << v << " ";
        }
        cout << endl;
    }
}

int main()
{
    int n, m;
    cin >> n >> m;

    vector<pair<int, int>> edges(m);
    for (auto &[u, v] : edges)
    {
        cin >> u >> v;
    }

    find(n, edges);

    return 0;
}