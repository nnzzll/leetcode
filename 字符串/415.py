class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1)-1
        j = len(num2)-1
        res = []
        c = 0
        add = 0
        while(i>=0 or j>=0 or c!=0):
            x = ord(num1[i])-ord('0') if i>=0 else 0
            y = ord(num2[j])-ord('0') if j>=0 else 0
            add = x+y+c
            res.append(str(add%10))
            c = add//10
            i -=1
            j -=1
        res = res[::-1]
        return "".join(res)

num1 = "1"
num2 = "9"
obj = Solution()
obj.addStrings(num1,num2)