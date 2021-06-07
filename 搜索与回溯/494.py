from typing import List


class Solution:
    def __init__(self) -> None:
        self.count = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dfs(nums,0,0,target)
        return self.count

    def dfs(self,nums: list, idx, Sum: int, target: int):
        if(idx == len(nums)):
            if(Sum == target):
                self.count += 1
        else:
            self.dfs(nums, idx+1, Sum+nums[idx], target)
            self.dfs(nums, idx+1, Sum-nums[idx], target)


nums = [1, 1, 1, 1, 1]
target = 3
obj = Solution()
print(obj.findTargetSumWays(nums, target))
