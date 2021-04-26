#include <vector>
#include <iostream>
using namespace std;

//Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// 递归
class Recursion
{
public:
    vector<int> res;
    vector<int> preorderTraversal(TreeNode *root)
    {
        if (root)
        {
            res.push_back(root->val);
            preorderTraversal(root->left);
            preorderTraversal(root->right);
        }
        return res;
    }
};

// 迭代
class Iteration
{
public:
    vector<int> preorderTraversal(TreeNode *root)
    {
        if(!root)
            return {};
        vector<int> res;
        vector<TreeNode *> NodeStack;
        NodeStack.push_back(root);
        while (!NodeStack.empty())
        {
            TreeNode *node = NodeStack.back();
            res.push_back(node->val);
            NodeStack.pop_back();
            if (node->right)
                NodeStack.push_back(node->right);
            if (node->left)
                NodeStack.push_back(node->left);
        }
        return res;
    }
};

int main()
{
    TreeNode *root = new TreeNode(0);
    root->left = new TreeNode(1);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(4);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(5);
    root->right->right = new TreeNode(6);
    Iteration obj;
    vector<int> res = obj.preorderTraversal(root);
    for (auto num : res)
        cout << num << endl;
}