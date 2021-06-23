import math
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n-1
        dp = [0 for _ in range(n+1)]
        dp[2] = 1
        for i in range(4, n+1):
            for j in range(2, i):
                dp[i] = max(dp[i], max(j*(i-j), j*dp[i-j]))
        return dp[n]


class Greedy:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n-1
        a,b = n//3,n%3
        if(b==0):
            return math.pow(3,a)
        if(b==1):
            return math.pow(3,a-1)*4
        return math.pow(3,a)*2

n = 10
obj = Greedy()
print(obj.cuttingRope(n))
