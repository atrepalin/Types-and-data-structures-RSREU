#include <iostream>
#include <vector>
#include <sstream>

void BubbleSort(std::vector<int> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i)
    {
        for (int j = 0; j < n - i - 1; ++j)
        {
            if (arr[j] < arr[j + 1])
            {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int main()
{
    std::string input;
    std::getline(std::cin, input);

    std::istringstream iss(input);
    std::vector<int> inputList;
    int number;

    while (iss >> number)
    {
        inputList.push_back(number);
    }

    BubbleSort(inputList);

    for (const int &num : inputList)
    {
        std::cout << num << " ";
    }

    return 0;
}