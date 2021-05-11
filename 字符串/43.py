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

    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        j = len(num2)-1
        res = []
        c = 0
        result = 0
        while(j>=0):
            i = len(num1)-1
            temp = []
            y = ord(num2[j])-ord('0')
            while(i>=0 or c!=0):
                x = ord(num1[i])-ord('0') if i>=0 else 0
                result = x*y+c
                temp.append(str(result%10))
                c = result//10
                i -= 1
            temp = temp[::-1]
            for _ in range(len(num2)-1-j):
                temp.append('0')
            res.append("".join(temp))
            j-=1
        print(res)
        ans = res[0]
        for i in range(1,len(res)):
            ans = self.addStrings(ans,res[i])
        return ans
num1 = "1210"
num2 = "291"
obj = Solution()
obj.multiply(num1,num2)