#include <vector>
#include <numeric>
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
    bool hasPathSum(TreeNode *root, int targetSum)
    {
        if (!root)
            return false;
        if (!root->left && !root->right)
            return targetSum == root->val;
        return hasPathSum(root->left, targetSum - root->val) || hasPathSum(root->right, targetSum - root->val);
    }
};

class BackTracking
{
public:
    bool hasPathSum(TreeNode *root, int targetSum)
    {
        vector<int> path;
        dfs(root, targetSum, path);
    }

    bool dfs(TreeNode *root, int targetSum, vector<int> path)
    {
        if (!root)
            return false;
        path.push_back(root->val);
        if (!root->left && !root->right)
        {
            int Sum = accumulate(path.begin(), path.end(), 0);
            return Sum == targetSum;
        }
        return dfs(root->left, targetSum, path) || dfs(root->right, targetSum, path);
    }
};