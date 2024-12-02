#include <iostream>
#include <vector>
#include <sstream>
#include <map>

void CountSort(std::vector<int> &arr)
{
    int n = arr.size();

    std::map<int, int> count;

    for (int num : arr)
    {
        count[num]++;
    }

    int index = 0;
    for (const auto &pair : count)
    {
        int value = pair.first;
        int occurrences = pair.second;
        for (int i = 0; i < occurrences; ++i)
        {
            arr[index++] = value;
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

    CountSort(inputList);

    for (const int &num : inputList)
    {
        std::cout << num << " ";
    }

    return 0;
}