'''
    二叉树的中序遍历
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
class Recursion:
    def inorderTraversal(self, root: TreeNode) -> list:
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root, res):
        if(root):
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)


# 迭代
class Iteration:
    def inorderTraversal(self, root: TreeNode) -> list:
        res = []
        stack = []
        while(stack or root):
            if(root):
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res



root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
obj = Iteration()
print(obj.inorderTraversal(root))
