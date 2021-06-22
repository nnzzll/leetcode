from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        参考:https://zhuanlan.zhihu.com/p/48085706
        """
        i = len(nums)-2
        while(i>=0 and nums[i]>=nums[i+1]):
            i -= 1
        if i>=0:
            j = len(nums)-1
            while(i<j and nums[j]<=nums[i]):
                j -= 1
            nums[i],nums[j] = nums[j],nums[i]
        
        end = len(nums)-1
        start = i+1
        while(start<end):
            nums[start],nums[end] = nums[end],nums[start]
            end -= 1
            start += 1


nums = [3,4,5,7,7,6]
obj = Solution()
obj.nextPermutation(nums)
print(nums)