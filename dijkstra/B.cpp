#include <queue>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

#define INF 2009000999

struct Edge
{
    int to;
    int weight;
};

struct State
{
    int vertex;
    int distance;
};

bool operator<(const State &a, const State &b)
{
    return a.distance > b.distance;
}

vector<int> dijkstra(vector<vector<Edge>> &graph, int start, int n)
{
    vector<int> distances(n, INF);
    distances[start] = 0;
    priority_queue<State> priority_queue;
    priority_queue.push({start, 0});

    while (!priority_queue.empty())
    {
        State current_state = priority_queue.top();
        priority_queue.pop();

        if (current_state.distance > distances[current_state.vertex])
        {
            continue;
        }

        for (const Edge &edge : graph[current_state.vertex])
        {
            int distance = current_state.distance + edge.weight;
            if (distance < distances[edge.to])
            {
                distances[edge.to] = distance;
                priority_queue.push({edge.to, distance});
            }
        }
    }

    return distances;
}

int main()
{
    int num;
    cin >> num;

    for (int i = 0; i < num; i++)
    {
        int n, m;
        cin >> n >> m;

        vector<vector<Edge>> graph(n);
        for (int j = 0; j < m; j++)
        {
            int u, v, w;
            cin >> u >> v >> w;
            graph[u].push_back({v, w});
            graph[v].push_back({u, w});
        }

        int start;
        cin >> start;

        vector<int> distances = dijkstra(graph, start, n);
        for (int j = 0; j < n; j++)
        {
            cout << distances[j] << " ";
        }
        cout << endl;
    }

    return 0;
}