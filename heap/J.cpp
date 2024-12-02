#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <unordered_map>

namespace aboba = std;

struct Event
{
    int pos;
    int index;
    bool is_start;

    bool operator<(const Event &other) const
    {
        if (pos == other.pos)
            return is_start > other.is_start;
        return pos < other.pos;
    }
};

int main()
{
    int N, W;
    aboba::cin >> N >> W;

    aboba::vector<Event> events;
    aboba::vector<int> figureWidths(N);

    for (int i = 0; i < N; ++i)
    {
        int a, w;
        aboba::cin >> a >> w;
        events.push_back({a, i, true});
        events.push_back({a + w - 1, i, false});
        figureWidths[i] = w;
    }

    sort(events.begin(), events.end());

    aboba::priority_queue<int, aboba::vector<int>, aboba::greater<int>> free_heights;
    aboba::unordered_map<int, int> figure_height_map;
    aboba::vector<aboba::vector<int>> figure_positions;
    int max_height = 0;

    for (const auto &event : events)
    {
        if (event.is_start)
        {
            int height;
            if (!free_heights.empty())
            {
                height = free_heights.top();
                free_heights.pop();
            }
            else
            {
                height = max_height++;
                figure_positions.emplace_back();
            }
            figure_height_map[event.index] = height;
            figure_positions[height].push_back(event.index + 1);
        }
        else
        {
            int height = figure_height_map[event.index];
            free_heights.push(height);
        }
    }

    int min_height = max_height;
    aboba::cout << min_height << aboba::endl;

    for (int h = 0; h < min_height; ++h)
    {
        for (int fig : figure_positions[h])
        {
            aboba::cout << fig << " ";
        }
    }
    aboba::cout << aboba::endl;

    return 0;
}