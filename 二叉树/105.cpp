#include <vector>
#include <queue>
#include <string>
#include <unordered_map>
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
    unordered_map<int, int> idx;
    int preIdx = 0;
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder)
    {

        int n = inorder.size();
        for (int i = 0; i < n; i++)
            idx[inorder[i]] = i;
        return build(preorder, inorder,0, n - 1);
    }

    TreeNode* build(vector<int>& preorder, vector<int>& inorder, int begin, int end)
    {
        if (begin<=end)
        {
            int val = preorder[preIdx];
            TreeNode* root = new TreeNode(val);
            int inIdx = idx[val];
            preIdx++;
            root->left = build(preorder, inorder, begin, inIdx-1);
            root->right = build(preorder, inorder,inIdx + 1, end);
            return root;
        }
        return nullptr;
    }
};
string treeNodeToString(TreeNode *root)
{
    if (root == nullptr)
    {
        return "[]";
    }

    string output = "";
    queue<TreeNode *> q;
    q.push(root);
    while (!q.empty())
    {
        TreeNode *node = q.front();
        q.pop();

        if (node == nullptr)
        {
            output += "null, ";
            continue;
        }

        output += to_string(node->val) + ", ";
        q.push(node->left);
        q.push(node->right);
    }
    return "[" + output.substr(0, output.length() - 2) + "]";
}

