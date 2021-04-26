# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
class Recursion:
    def postorderTraversal(self, root: TreeNode) -> list:
        res = []
        self.postorder(root, res)
        return res

    def postorder(self, root, res):
        if(root):
            self.postorder(root.left, res)
            self.postorder(root.right, res)
            res.append(root.val)

# 迭代
class Iteration:
    def postorderTraversal(self, root: TreeNode) -> list:
        res = []
        stack = []
        if(root):
            stack.append(root)
        while(stack):
            node = stack.pop()
            res.append(node.val)
            if(node.left):
                stack.append(node.left)
            if(node.right):
                stack.append(node.right)
        res =res[::-1]

        return res


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
obj = Iteration()
print(obj.postorderTraversal(root))