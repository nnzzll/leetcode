import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        deque = collections.deque([root])
        cnt = 1
        while(deque):
            temp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if cnt%2==0:
                    temp.append(node.val)
                else:
                    temp.appendleft(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(list(temp))
        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.levelOrder(root))