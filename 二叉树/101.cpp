#include <queue>
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

class DFS
{
public:
    bool isSymmetric(TreeNode *root)
    {
        if (root)
            return dfs(root->left, root->right);
        else
            return true;
    }

    bool dfs(TreeNode *left, TreeNode *right)
    {
        if ((left == nullptr) && (right == nullptr))
            return true;
        else if (left && right && dfs(left->left, right->right) && dfs(left->right, right->left) && (left->val == right->val))
            return true;
        else
            return false;
    }
};

class BFS
{
public:
    bool isSymmetric(TreeNode *root)
    {
        queue<TreeNode *> q;
        TreeNode *left, *right;
        left = root;
        right = root;
        q.push(left);
        q.push(right);
        while (q.size())
        {
            left = q.front();
            q.pop();
            right = q.front();
            q.pop();
            if(left==nullptr && right==nullptr)
                continue;
            if((!left||!right)||(left->val!=right->val))
                return false;
            q.push(left->left);
            q.push(right->right);
            q.push(left->right);
            q.push(right->left);
        }
        return true;
    }
};

int main()
{
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(2);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(4);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(3);
    BFS obj;
    cout<<obj.isSymmetric(root);
}