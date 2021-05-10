# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        res1 = []
        res2 = []
        def dfs(root,res):
            if(root):
                if(not root.left and not root.right):
                    res.append(root.val)
                    return
                else:
                    dfs(root.left,res)
                    dfs(root.right,res)
            else:
                return 
        dfs(root1,res1)
        dfs(root2,res2)
        return res1==res2


root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
root1.right = TreeNode(1)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)
obj = Solution()
print(obj.leafSimilar(root1,root2))