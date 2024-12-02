#include <iostream>
#include <vector>
#include <sstream>

int BubbleSort(std::vector<int> &arr)
{
    int swaps = 0;
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i)
    {
        for (int j = 0; j < n - i - 1; ++j)
        {
            if (arr[j] > arr[j + 1])
            {
                std::swap(arr[j], arr[j + 1]);
                swaps++;
            }
        }
    }

    return swaps;
}

int main()
{
    int n = 0;

    std::cin >> n;
    std::cin.ignore();

    std::string input;
    std::getline(std::cin, input);

    std::istringstream iss(input);
    std::vector<int> inputList;
    int number;

    while (iss >> number)
    {
        inputList.push_back(number);
    }

    int swaps = BubbleSort(inputList);

    std::cout << swaps;

    return 0;
}