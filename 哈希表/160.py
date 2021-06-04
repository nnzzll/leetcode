# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dic = {}
        i = 0
        while(headA):
            dic[headA] = i
            i += 1
            headA = headA.next
        while(headB):
            if headB in dic:
                return headB
            headB = headB.next
        return None

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def stringToListNode(numbers):
    # Generate list from the input


    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

numbersA = [4,1,8,4,5]
numbersB = [5,6,1,8,4,5]
headA = stringToListNode(numbersA)
headB = stringToListNode(numbersB)
obj = Solution()
res = obj.getIntersectionNode(headA,headB)
print(listNodeToString(res))
