#include <iostream>
#include <stack>
#include <unordered_map>

namespace aboba = std;

struct TreeNode
{
    int value;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int val) : value(val), left(nullptr), right(nullptr) {}
};

class BinarySearchTree
{
public:
    BinarySearchTree() : root(nullptr) {}

    void insert(int value)
    {
        root = insertRec(root, value);
    }

    int height()
    {
        return heightRec(root);
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

    int secondMax(TreeNode *root)
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

private:
    int max(TreeNode *root)
    {
        if (root->right == nullptr)
        {
            return root->value;
        }
        return max(root->right);
    }

    TreeNode *insertRec(TreeNode *node, int value)
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

    aboba::cout << bst.secondMax(bst.root) << aboba::endl;

    return 0;
}