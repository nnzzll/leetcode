# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFS:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left:TreeNode,right:TreeNode):
            if(left==None and right==None):
                return True
            elif(left and right and dfs(left.left,right.right) and dfs(left.right,right.left) and left.val==right.val):
                return True
            else:
                return False
        if(root):
            return dfs(root.left,root.right)
        else:
            return True

class BFS:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root]
        while(queue):
            layer = []
            length = len(queue)
            while(length):
                node = queue.pop(0)
                if(node):
                    layer.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    layer.append(None)
                length -= 1

            if layer == layer[::-1]:
                continue
            else:
                return False
        return True

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(1)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
obj = BFS()
print(obj.isSymmetric(root))
