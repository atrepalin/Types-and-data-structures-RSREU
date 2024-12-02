#include <iostream>
#include <vector>
#include <string>

namespace aboba = std;

class MinHeap
{
private:
    aboba::vector<int> heap;

    void siftUp(int i)
    {
        int p = (i - 1) / 2;
        while (i > 0 && heap[i] < heap[p])
        {
            aboba::swap(heap[i], heap[p]);
            i = p;
            p = (i - 1) / 2;
        }
    }

    void siftDown(int i)
    {
        while (2 * i + 1 < heap.size())
        {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            int j = left;

            if (right < heap.size() && heap[right] < heap[left])
                j = right;

            if (heap[i] <= heap[j])
                break;

            aboba::swap(heap[i], heap[j]);
            i = j;
        }
    }

public:
    void clear()
    {
        heap.clear();
    }

    void insert(int x)
    {
        heap.push_back(x);
        siftUp(heap.size() - 1);
    }

    int extract()
    {
        int removed = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        siftDown(0);
        return removed;
    }

    bool isEmpty() const
    {
        return heap.empty();
    }
};

int main()
{
    MinHeap heap;
    int x;
    aboba::string cmd;

    while (aboba::cin >> cmd)
    {
        if (cmd == "CLEAR")
        {
            heap.clear();
        }
        else if (cmd == "ADD")
        {
            aboba::cin >> x;
            heap.insert(x);
        }
        else if (cmd == "EXTRACT")
        {
            if (heap.isEmpty())
            {
                aboba::cout << "CANNOT" << aboba::endl;
            }
            else
            {
                aboba::cout << heap.extract() << aboba::endl;
            }
        }
    }

    return 0;
}