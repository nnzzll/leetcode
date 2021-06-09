from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        Sum = 0
        for num in nums:
            Sum += num
        if (Sum-target)<0 or (Sum-target)%2!=0:
            return 0
        total = (Sum-target)//2
        dp = [[0 for _ in range(total+1)] for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for i in range(1,len(nums)+1):
            num = nums[i-1]
            for j in range(total+1):
                if(j>=num):
                    dp[i][j] = dp[i-1][j]+dp[i-1][j-num]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)][total]
        
nums = [1,1,1,1,1]
target = 3
obj = Solution()
print(obj.findTargetSumWays(nums,target))