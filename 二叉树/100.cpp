#include<queue>
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
    bool isSameTree(TreeNode *p, TreeNode *q)
    {
        if ((p && !q) || (!p && q))
            return false;
        else if (!p && !q)
            return true;
        else
        {
            if (p->val == q->val)
                return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
            else
                return false;
        }
    }
};

class BFS
{
public:
    bool isSameTree(TreeNode*p,TreeNode*q)
    {
        queue<TreeNode*> NodeList;
        NodeList.push(p);
        NodeList.push(q);
        while(!NodeList.empty())
        {
            p = NodeList.front();
            NodeList.pop();
            q = NodeList.front();
            NodeList.pop();
            if ((p && !q) || (!p && q))
                return false;
            if(!p&&!q)
                continue;
            if(p->val!=q->val)
                return false;
            NodeList.push(p->left);
            NodeList.push(q->left);
            NodeList.push(p->right);
            NodeList.push(q->right);
        }
        return true;
    }
};