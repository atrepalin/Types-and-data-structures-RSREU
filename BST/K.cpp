#include <iostream>
#include <stack>
#include <unordered_map>
#include <vector>
#include <algorithm>

namespace aboba = std;

struct TreeNode
{
    long long value;
    TreeNode *left;
    TreeNode *right;

    TreeNode(long long val) : value(val), left(nullptr), right(nullptr) {}
};

class BinarySearchTree
{
public:
    BinarySearchTree() : root(nullptr) {}

    void insert(long long value)
    {
        root = insertRec(root, value);
    }

    int height()
    {
        return heightRec(root);
    }

    long long lowerBound(long long i)
    {
        TreeNode *current = root;
        long long result = -1;
        while (current != nullptr)
        {
            if (current->value >= i)
            {
                result = current->value;
                current = current->left;
            }
            else
            {
                current = current->right;
            }
        }
        return result;
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
                size++;
                stack.push(current->right);
                stack.push(current->left);
            }
        }
        return size;
    }

    long long secondMax(TreeNode *root)
    {
        if (root == nullptr)
        {
            return -1;
        }

        if (root->right == nullptr && root->left != nullptr)
        {
            return max(root->left);
        }

        if (root->right != nullptr)
        {
            if (root->right->right == nullptr && root->right->left == nullptr)
            {
                return root->value;
            }
        }

        return secondMax(root->right);
    }

    TreeNode *root;

    aboba::vector<long long> orderUp(TreeNode *node)
    {
        aboba::vector<long long> result;
        if (node == nullptr)
        {
            return result;
        }

        auto left = orderUp(node->left);
        result.insert(result.end(), left.begin(), left.end());

        result.push_back(node->value);

        auto right = orderUp(node->right);
        result.insert(result.end(), right.begin(), right.end());

        return result;
    }

    aboba::vector<long long> leaves(TreeNode *node)
    {
        aboba::vector<long long> result;
        if (node == nullptr)
        {
            return result;
        }

        if (node->left == nullptr && node->right == nullptr)
        {
            result.push_back(node->value);
            return result;
        }

        auto left = leaves(node->left);
        result.insert(result.end(), left.begin(), left.end());

        auto right = leaves(node->right);
        result.insert(result.end(), right.begin(), right.end());

        return result;
    }

    aboba::vector<long long> forks(TreeNode *node)
    {
        aboba::vector<long long> result;
        if (node == nullptr)
        {
            return result;
        }

        auto left = forks(node->left);
        result.insert(result.end(), left.begin(), left.end());

        if (node->left != nullptr && node->right != nullptr)
        {
            result.push_back(node->value);
        }

        auto right = forks(node->right);
        result.insert(result.end(), right.begin(), right.end());

        aboba::sort(result.begin(), result.end());
        return result;
    }

    aboba::vector<long long> branches(TreeNode *node)
    {
        aboba::vector<long long> result;
        if (node == nullptr)
        {
            return result;
        }

        auto left = branches(node->left);
        result.insert(result.end(), left.begin(), left.end());

        if ((node->left != nullptr) + (node->right != nullptr) == 1)
        {
            result.push_back(node->value);
        }

        auto right = branches(node->right);
        result.insert(result.end(), right.begin(), right.end());

        aboba::sort(result.begin(), result.end());
        return result;
    }

    bool isBalanced(TreeNode *root)
    {
        if (root == nullptr)
        {
            return true;
        }

        int leftHeight = heightRec(root->left);
        int rightHeight = heightRec(root->right);

        if (aboba::abs(leftHeight - rightHeight) > 1)
        {
            return false;
        }

        return isBalanced(root->left) && isBalanced(root->right);
    }

private:
    long long max(TreeNode *root)
    {
        if (root->right == nullptr)
        {
            return root->value;
        }
        return max(root->right);
    }

    TreeNode *insertRec(TreeNode *node, long long value)
    {
        if (node == nullptr)
        {
            return new TreeNode(value);
        }
        if (value < node->value)
        {
            node->left = insertRec(node->left, value);
        }
        else if (value > node->value)
        {
            node->right = insertRec(node->right, value);
        }
        return node;
    }

    int heightRec(TreeNode *node)
    {
        aboba::stack<TreeNode *> stack;
        aboba::unordered_map<TreeNode *, int> heights;
        stack.push(node);

        while (!stack.empty())
        {
            TreeNode *current = stack.top();
            if (current == nullptr)
            {
                stack.pop();
                heights[current] = -1;
            }
            else if (heights.find(current) != heights.end())
            {
                stack.pop();
                int leftHeight = heights[current->left];
                int rightHeight = heights[current->right];
                heights[current] = aboba::max(leftHeight, rightHeight) + 1;
            }
            else
            {
                stack.push(current->right);
                stack.push(current->left);
                heights[current] = 0;
            }
        }
        return heights[node] + 1;
    }
};

int main()
{
    BinarySearchTree bst;
    long long number, prev_ans;
    char op, prev;
    int n;

    aboba::cin >> n;

    for (int i = 0; i < n; ++i)
    {
        aboba::cin >> op;
        aboba::cin >> number;

        if (op == '+')
        {
            if (prev == '?')
            {
                bst.insert((number + prev_ans) % 1000000000ll);
            }
            else
            {
                bst.insert(number);
            }
        }
        else
        {
            prev_ans = bst.lowerBound(number);
            aboba::cout << prev_ans << aboba::endl;
        }

        prev = op;
    }

    return 0;
}