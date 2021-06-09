from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum = 0
        for num in nums:
            Sum += num
        if (Sum % 2 != 0) or len(nums)<2 or max(nums)>Sum//2:
            return False
        target = Sum//2
        dp = [[False for _ in range(target+1)] for _ in range(len(nums))]
        dp[0][nums[0]] = True
        for i in range(len(nums)):
            dp[i][0] = True
        for i in range(1,len(nums)):
            for j in range(target+1):
                if j>=nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)-1][target]


nums = [1,5,11,5]
obj = Solution()
print(obj.canPartition(nums))