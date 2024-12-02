#include <iostream>
#include <vector>
#include <sstream>

void SelectionSort(std::vector<int> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n; ++i)
    {
        int maxIndex = i;
        for (int j = i + 1; j < n; ++j)
        {
            if (arr[j] > arr[maxIndex])
            {
                maxIndex = j;
            }
        }
        std::swap(arr[i], arr[maxIndex]);
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

    SelectionSort(inputList);

    for (const int &num : inputList)
    {
        std::cout << num << " ";
    }

    return 0;
}