#include <queue>
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

//BFS
class BFS
{
public:
    int maxDepth(TreeNode *root)
    {
        queue<TreeNode *> q;
        int depth = 0;
        if (root)
            q.push(root);
        while (!q.empty())
        {
            int length = q.size();
            for (int i = 0; i < length; i++)
            {
                TreeNode *node = q.front();
                q.pop();
                if (node->left)
                    q.push(node->left);
                if (node->right)
                    q.push(node->right);
            }
            depth++;
        }
        return depth;
    }
};

class DFS
{
    int maxDepth(TreeNode *root)
    {
        if(root)
        {
            int left = maxDepth(root->left);
            int right = maxDepth(root->right);
            return max(left,right)+1;
        }
        else
            return 0;
    }
};