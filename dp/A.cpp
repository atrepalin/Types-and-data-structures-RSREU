#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> dp(n), cost(n);
    for (int i = 0; i < n; ++i)
        cin >> cost[i];

    dp[0] = cost[0];
    dp[1] = cost[1];

    for (int i = 2; i < n; ++i)
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i];

    cout << dp[n - 1] << endl;
    return 0;
}