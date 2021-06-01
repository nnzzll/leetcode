from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        def dfs(root, target, res, path):
            if not root:
                return
            if not root.left and not root.right:
                if sum(path)+root.val == target:
                    res.append(path+[root.val])
                return
            dfs(root.left, target, res, path+[root.val])
            dfs(root.right, target, res, path+[root.val])
        res = []
        dfs(root, target, res, [])
        return res


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


root = stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,null,1]")
targetSum = 22
obj = Solution()
print(obj.pathSum(root, targetSum))
