class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        for i in range(1,n):
            num = start+2*i
            ans = ans^num
        return ans

n = 10
start = 5
obj = Solution()
print(obj.xorOperation(n,start))