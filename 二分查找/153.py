'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。
请找出其中最小的元素。
'''

class Solution:
    def findMin(self, nums) -> int:
        l = 0
        r = len(nums)-1
        while(l<r):
            mid = l + (r-l)//2
            if(nums[mid]>nums[r]):
                l = mid+1
            if(nums[mid]<=nums[r]):
                r = mid
        return nums[l]

nums=[3,1,2]
obj = Solution()
print(obj.findMin(nums))
