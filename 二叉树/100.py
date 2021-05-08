# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFS:
    def isSameTree(p: TreeNode, q: TreeNode) -> bool:
        if(p and not q) or (not p and q):
            return False
        elif (not p and not q):
            return True
        elif (p.val != q.val):
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class BFS:
    def isSameTree(p: TreeNode, q: TreeNode) -> bool:
        NodeList = []
        NodeList.append(p)
        NodeList.append(q)
        while(NodeList):
            p = NodeList.pop(0)
            q = NodeList.pop(0)
            if(p and not q) or (not p and q):
                return False
            elif (p.val != q.val):
                return False
            elif (not p and not q):
                continue
            else:
                NodeList.append(p.left)
                NodeList.append(q.left)
                NodeList.append(p.right)
                NodeList.append(q.right)
        return True