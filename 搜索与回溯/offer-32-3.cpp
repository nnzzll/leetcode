#include<vector>
#include<deque>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(!root)
            return {{}};
        vector<vector<int>>result;
        deque<TreeNode*>queue;
        queue.push_back(root);
        bool flag=true;
        while(!queue.empty()){
            vector<int>tmp;
            int length = queue.size();
            for(int i=0;i<length;i++){
                TreeNode* node = queue.front();
                queue.pop_front();
                tmp.push_back(node->val);
                if(node->left)
                    queue.push_back(node->left);
                if(node->right)
                    queue.push_back(node->right);
            }
            if(flag)
                result.push_back(tmp);
            else{
                reverse(tmp.begin(),tmp.end());
                result.push_back(tmp);
            }
            flag = !flag;
        }
        return result;
    }
};