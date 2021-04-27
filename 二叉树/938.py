'''
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sumBST = 0
        stack = []
        while(stack or root):
            if(root):
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if(root.val>=low and root.val<=high):
                    sumBST+=root.val
                root = root.right
        return sumBST




root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right = TreeNode(15)
root.right.right = TreeNode(18)
obj = Solution()
print(obj.rangeSumBST(root,7,15))