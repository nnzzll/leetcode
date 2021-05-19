class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0 for _ in range(n)]
        dp[0] = 1
        p = [0,0,0]
        for i in range(1,n):
            dp[i] = min(dp[p[0]]*2,dp[p[1]]*3,dp[p[2]]*5)
            for idx,num in enumerate([dp[p[0]]*2,dp[p[1]]*3,dp[p[2]]*5]):
                if dp[i] == num:
                    p[idx]+=1
        return dp

n = 10
obj = Solution()
print(obj.nthUglyNumber(n))