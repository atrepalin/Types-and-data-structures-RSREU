#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    string text;
    cin >> text;

    string modified_text = "#";
    for (char c : text)
    {
        modified_text += c;
        modified_text += '#';
    }

    int n = modified_text.size();
    vector<int> p(n, 0);
    int center = 0, right = 0;

    for (int i = 0; i < n; ++i)
    {
        int mirror = 2 * center - i;

        if (i < right)
        {
            p[i] = min(right - i, p[mirror]);
        }

        while (i + p[i] + 1 < n && i - p[i] - 1 >= 0 &&
               modified_text[i + p[i] + 1] == modified_text[i - p[i] - 1])
        {
            p[i]++;
        }

        if (i + p[i] > right)
        {
            center = i;
            right = i + p[i];
        }
    }

    for (int i = 1; i < n; i += 2)
    {
        cout << p[i] << ' ';
    }
    cout << endl;

    return 0;
}