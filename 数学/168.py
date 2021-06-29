class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dic = {}
        for i in range(1,27):
            dic[i] = chr(ord("A")+(i-1))

        res = []
        while(columnNumber):
            mod = columnNumber%26
            if mod:
                res.append(dic[mod])
                columnNumber//=26
            else:
                res.append("Z")
                columnNumber//=26
                columnNumber-=1
        return "".join(res[::-1])

obj = Solution()
columnNumber=30
print(obj.convertToTitle(columnNumber))