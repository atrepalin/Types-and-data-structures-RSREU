#include <iostream>
#include <vector>
#include <algorithm>

namespace aboba = std;

bool canInflate(int M,
                const aboba::vector<int> &T,
                const aboba::vector<int> &Z,
                const aboba::vector<int> &Y,
                long long time_limit,
                aboba::vector<long long> &balloons)
{
    long long total_balloons = 0;

    for (size_t i = 0; i < T.size(); ++i)
    {
        long long T_i = T[i];
        long long Z_i = Z[i];
        long long Y_i = Y[i];

        long long full_cycles = time_limit / (T_i * Z_i + Y_i);
        long long balloons_in_full_cycles = full_cycles * Z_i;

        long long remaining_time = time_limit % (T_i * Z_i + Y_i);
        long long additional_balloons = aboba::min(Z_i, remaining_time / T_i);

        long long b = balloons_in_full_cycles + additional_balloons;

        balloons[i] = b;

        total_balloons += b;
    }

    return total_balloons >= M;
}

int main()
{
    int M, N;
    aboba::cin >> M >> N;

    aboba::vector<int> T(N), Z(N), Y(N);

    for (int i = 0; i < N; ++i)
    {
        aboba::cin >> T[i] >> Z[i] >> Y[i];
    }

    long long left = 0;
    long long right = 1e18;

    aboba::vector<long long> balloons(N);
    aboba::vector<long long> answer;

    while (left < right)
    {
        long long mid = left + (right - left) / 2;

        if (canInflate(M, T, Z, Y, mid, balloons))
        {
            right = mid;
            answer = balloons;
        }
        else
        {
            left = mid + 1;
        }
    }

    aboba::cout << left << aboba::endl;

    long long current_total = 0;

    for (auto b : answer)
    {
        current_total += b;
    }

    for (int i = 0; i < N && current_total > M; i++)
    {
        int reduce = aboba::min(answer[i], current_total - M);
        answer[i] -= reduce;
        current_total -= reduce;
    }

    for (auto b : answer)
    {
        aboba::cout << b << " ";
    }

    return 0;
}