#include <vector>
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

class Solution
{
public:
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        queue<TreeNode *> NodeList;
        vector<vector<int>> result;

        int layer_length;
        if (root)
            NodeList.push(root);
        while (!NodeList.empty())
        {
            vector<int> layer;
            layer_length = NodeList.size();
            for (int i = 0; i < layer_length; i++)
            {
                TreeNode *Node = NodeList.front();
                NodeList.pop();
                layer.push_back(Node->val);
                if (Node->left)
                    NodeList.push(Node->left);
                if (Node->right)
                    NodeList.push(Node->right);
            }
            result.push_back(layer);
        }
        return result;
    }
};