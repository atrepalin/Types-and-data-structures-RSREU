#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <unordered_map>

using namespace std;

const long long INF = numeric_limits<long long>::max();

int main()
{
    int N, K;
    cin >> N >> K;

    vector<vector<pair<int, int>>> graph(N + 1);

    for (int i = 0; i < K; ++i)
    {
        int a, b, l;
        cin >> a >> b >> l;
        graph[a].emplace_back(b, l);
        graph[b].emplace_back(a, l);
    }

    int A, B;
    cin >> A >> B;

    vector<long long> dist(N + 1, INF);
    dist[A] = 0;

    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    pq.push({0, A});

    while (!pq.empty())
    {
        auto [current_dist, current_node] = pq.top();
        pq.pop();

        if (current_dist > dist[current_node])
        {
            continue;
        }

        for (const auto &[neighbor, weight] : graph[current_node])
        {
            long long new_dist = current_dist + weight;
            if (new_dist < dist[neighbor])
            {
                dist[neighbor] = new_dist;
                pq.push({new_dist, neighbor});
            }
        }
    }

    cout << (dist[B] == INF ? -1 : dist[B]) << endl;

    return 0;
}