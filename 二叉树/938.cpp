#include <stack>
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
class Solution
{
public:
    int rangeSumBST(TreeNode *root, int low, int high)
    {
        stack<TreeNode *> stk;
        int sumBST = 0;
        while (!stk.empty() || root)
        {
            if (root)
            {
                stk.push(root);
                root = root->left;
            }
            else
            {
                root = stk.top();
                if (root->val >= low && root->val <= high)
                    sumBST += root->val;
                stk.pop();
                root = root->right;
            }
        }
        return sumBST;
    }
};