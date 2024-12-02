#include <iostream>
#include <stack>
#include <unordered_map>
#include <vector>
#include <algorithm>

namespace aboba = std;

struct TreeNode
{
    int value;
    int count;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int val, int cnt) : value(val), count(cnt), left(nullptr), right(nullptr) {}
};

class BinarySearchTree
{
public:
    BinarySearchTree() : root(nullptr) {}

    void insert(int value)
    {
        root = insertRec(root, value, 1);
    }

    int size()
    {
        int size = 0;
        aboba::stack<TreeNode *> stack;
        stack.push(root);
        while (!stack.empty())
        {
            TreeNode *current = stack.top();
            stack.pop();
            if (current != nullptr)
            {
                size += current->count;
                stack.push(current->right);
                stack.push(current->left);
            }
        }
        return size;
    }

    TreeNode *root;

    aboba::vector<TreeNode> orderUp(TreeNode *node)
    {
        aboba::vector<TreeNode> result;
        if (node == nullptr)
        {
            return result;
        }

        auto left = orderUp(node->left);
        result.insert(result.end(), left.begin(), left.end());

        result.push_back(*node);

        auto right = orderUp(node->right);
        result.insert(result.end(), right.begin(), right.end());

        return result;
    }

private:
    TreeNode *insertRec(TreeNode *node, int value, int count)
    {
        if (node == nullptr)
        {
            return new TreeNode(value, count);
        }

        if (value < node->value)
        {
            node->left = insertRec(node->left, value, count);
        }
        else if (value > node->value)
        {
            node->right = insertRec(node->right, value, count);
        }
        else
        {
            node->count += count;
        }

        return node;
    }
};

int main()
{
    BinarySearchTree bst;
    int number;
    while (true)
    {
        aboba::cin >> number;
        if (number == 0)
        {
            break;
        }
        bst.insert(number);
    }

    auto sorted = bst.orderUp(bst.root);

    for (int i = 0; i < sorted.size(); i++)
    {
        aboba::cout << sorted[i].value << " " << sorted[i].count << "\n";
    }

    return 0;
}