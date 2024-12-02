#include <iostream>
#include <vector>
#include <string>
#include <queue>

namespace aboba = std;

int main()
{
    aboba::priority_queue<int> heap;
    int x;
    aboba::string cmd;

    while (aboba::cin >> cmd)
    {
        if (cmd == "CLEAR")
        {
            while (!heap.empty())
            {
                heap.pop();
            }
        }
        else if (cmd == "ADD")
        {
            aboba::cin >> x;
            heap.push(x);
        }
        else if (cmd == "EXTRACT")
        {
            if (heap.empty())
            {
                aboba::cout << "CANNOT" << aboba::endl;
            }
            else
            {
                aboba::cout << heap.top() << aboba::endl;
                heap.pop();
            }
        }
    }

    return 0;
}