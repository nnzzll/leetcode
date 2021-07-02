from typing import List


class Solution:
    def _printNumbers(self, n: int) -> List[int]:
        return list(range(1, 10**n))

    def printNumbers(self, n: int) -> List[int]:
        '''全排列'''
        num = ['0' for _ in range(n)]
        res = []
        def dfs(x):
            if x==n:
                ptr = 0
                while(ptr<n and num[ptr]=='0'):
                    ptr += 1
                if(ptr!=n):
                    res.append(int("".join(num[ptr:])))
                return
            for i in range(10):
                num[x] = str(i)
                dfs(x+1)
        dfs(0)
        return res
n = 2
obj = Solution()
print(obj.printNumbers(n))
