#include <iostream>
#include <vector>
#include <sstream>

void InsertionSort(std::vector<int> &arr)
{
    int n = arr.size();
    for (int i = 1; i < n; ++i)
    {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
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

    InsertionSort(inputList);

    for (const int &num : inputList)
    {
        std::cout << num << " ";
    }

    return 0;
}