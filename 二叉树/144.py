'''
    二叉树的前序遍历
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
class Recursion:
    def preorderTraversal(self, root: TreeNode) -> list:
        res = []
        self.preorder(root, res)
        return res

    def preorder(self, root, res):
        if(root):
            res.append(root.val)
            self.preorder(root.left, res)
            self.preorder(root.right, res)


# 递归
class Iteration:
    def preorderTraversal(self, root: TreeNode) -> list:
        res = []
        stack = []
        if(root):
            stack.append(root)
        while(stack):
            node = stack.pop()
            res.append(node.val)
            if(node.right):
                stack.append(node.right)
            if(node.left):
                stack.append(node.left)
        return res

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
obj = Iteration()
print(obj.preorderTraversal(root))
