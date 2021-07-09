from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        right = sum(nums)
        left = max(nums)
        def check(nums,temp,m):
            _temp_sum = 0
            cnt = 1
            for i in range(len(nums)):
                if _temp_sum+nums[i]>temp:
                    cnt+=1
                    _temp_sum = nums[i]
                else:
                    _temp_sum += nums[i]
            return cnt<=m
        while(left<right):
            mid = left + (right-left)//2
            if check(nums,mid,m):
                right = mid
            else:
                left = mid+1
        return left
nums = [1,2,3,4,5]
m = 2
obj = Solution()
print(obj.splitArray(nums,m))