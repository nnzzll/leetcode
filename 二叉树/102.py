# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
class Solution:
    def levelOrder(self, root: TreeNode):
        queue = []
        res = []
        if(root):
            queue.append(root)
        while(queue):
            temp = []
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                temp.append(node.val)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            res.append(temp)
        return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.levelOrder(root))
