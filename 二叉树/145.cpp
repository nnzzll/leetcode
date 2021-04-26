#include <vector>
#include <stack>
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
    vector<int> postorderTraversal(TreeNode *root)
    {
        if (root)
        {
            postorderTraversal(root->left);
            postorderTraversal(root->right);
            res.push_back(root->val);
        }
        return res;
    }
};

// 迭代
class Iteration
{
public:
    vector<int> postorderTraversal(TreeNode *root)
    {
        vector<int> res;
        stack<TreeNode *> NodeStack;
        NodeStack.push(root);
        while (!NodeStack.empty())
        {
            TreeNode *node = NodeStack.top();
            res.push_back(node->val);
            NodeStack.pop();
            if (node->left)
                NodeStack.push(node->left);
            if (node->right)
                NodeStack.push(node->right);
        }
        reverse(res.begin(),res.end());
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
    vector<int> res = obj.postorderTraversal(root);
    for (auto num : res)
        cout << num << endl;
}