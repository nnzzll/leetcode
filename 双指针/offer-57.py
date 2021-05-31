from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        while(l<r):
            if (nums[l] + nums[r])==target:
                return [nums[l],nums[r]]
            if (nums[l]+nums[r])<target:
                l+=1
            else:
                r-=1
        return []

