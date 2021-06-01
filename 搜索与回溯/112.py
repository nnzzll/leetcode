class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFS:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root:
            if not root.left and not root.right:
                return targetSum == root.val
            return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
        return False


class BackTracking:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        def dfs(root,targetSum,path:list):
            if not root:
                return False
            if not root.left and not root.right:
                return sum(path+[root.val])==targetSum
            return dfs(root.left,targetSum,path+[root.val]) or dfs(root.right,targetSum,path+[root.val])
        return dfs(root,targetSum,[])

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

obj = BackTracking()
print(obj.hasPathSum(root,targetSum))