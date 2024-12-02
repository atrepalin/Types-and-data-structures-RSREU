#include <iostream>
#include "math.h"

namespace aboba = std;

int main()
{
    double a, b, c, d;

    aboba::cin >> a >> b >> c >> d;

    double left = -1e10, right = 1e10;

    while (right - left > 1e-7)
    {
        double mid = (left + right) / 2;

        if (a * (a * aboba::pow(mid, 3) + b * aboba::pow(mid, 2) + c * mid + d) <= 0)
        {
            left = mid;
        }
        else
        {
            right = mid;
        }
    }

    aboba::cout << left << aboba::endl;
}