#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int PRIME = 31;
const int MOD = 1000000007;
const int ARR_SIZE = 1000000;

int hash_func(const string &s)
{
    long long hash = 0;

    for (char c : s)
    {
        hash = (hash * PRIME + (c - 'a' + 1)) % MOD;
    }

    return hash % ARR_SIZE;
}

vector<vector<string>> arr(ARR_SIZE);

int main()
{
    string inp;
    while (true)
    {
        getline(cin, inp);
        if (inp == "#")
            break;

        char op = inp[0];
        string word = inp.substr(2);

        int h = hash_func(word);

        if (op == '+')
        {
            arr[h].push_back(word);
        }
        else if (op == '-')
        {
            auto it = find(arr[h].begin(), arr[h].end(), word);
            if (it != arr[h].end())
            {
                arr[h].erase(it);
            }
        }
        else
        {
            auto it = find(arr[h].begin(), arr[h].end(), word);
            cout << (it != arr[h].end() ? "YES" : "NO") << endl;
        }
    }

    return 0;
}