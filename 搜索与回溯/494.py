from typing import List
from functools import lru_cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(idx,t):
            if idx == len(nums):
                return 1 if t==0 else 0
            return dfs(idx+1,t-nums[idx]) + dfs(idx+1,t+nums[idx])
        return dfs(0,target)

nums = [1, 1, 1, 1, 1]
target = 3
obj = Solution()
print(obj.findTargetSumWays(nums, target))
