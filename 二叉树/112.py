# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(node,Sum):
            if node:
                if(node.left==None and node.right==None):
                    return Sum-node.val==0
                else:
                    return dfs(node.left,Sum-node.val) or dfs(node.right,Sum-node.val)
            else:
                return False
        return dfs(root,targetSum)

root = TreeNode(1)
root.left = TreeNode(2)

obj = Solution()
targetSum = 2
print(obj.hasPathSum(root,targetSum))