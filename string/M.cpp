#include <iostream>
#include <vector>
using namespace std;

const int PRIME = 31;
const int MOD = 1e9 + 7;

vector<long long> prefix_hash, reverse_hash, power;

long long get_hash(int l, int r)
{
    return (prefix_hash[r] - prefix_hash[l] * power[r - l] % MOD + MOD) % MOD;
}

long long get_reverse_hash(int l, int r)
{
    return (reverse_hash[r] - reverse_hash[l] * power[r - l] % MOD + MOD) % MOD;
}

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> colors(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> colors[i];
    }

    prefix_hash.assign(n + 1, 0);
    reverse_hash.assign(n + 1, 0);
    power.assign(n + 1, 1);

    for (int i = 1; i <= n; ++i)
    {
        prefix_hash[i] = (prefix_hash[i - 1] * PRIME + colors[i - 1]) % MOD;
        reverse_hash[i] = (reverse_hash[i - 1] * PRIME + colors[n - i]) % MOD;
        power[i] = (power[i - 1] * PRIME) % MOD;
    }

    int middle = (n + 1) / 2;

    for (int i = middle; i >= 0; --i)
    {
        if (get_hash(0, i) == get_reverse_hash(n - 2 * i, n - i))
        {
            cout << (n - i) << " ";
        }
    }

    cout << endl;

    return 0;
}