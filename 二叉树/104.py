'''二叉树的最大深度'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        queue = []
        depth = 0
        if(root):
            queue.append(root)
        while(queue):
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            depth+=1
        return depth

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.maxDepth(root))