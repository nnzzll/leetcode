'''
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
'''
class Solution:
    def findMin(self, nums) -> int:
        l = 0 
        r = len(nums)-1 
        while(l+1<r):
            mid = l+(r-l)//2
            if(nums[mid]>nums[r]):
                l = mid + 1
            elif(nums[mid]<nums[r]):
                r = mid
            elif(nums[mid]>nums[l]):
                return nums[l]
            elif(nums[mid]==nums[l]):
                l+=1
                r-=1
            else:
                if(nums[mid]>=nums[mid-1]):
                    r = mid-1
                else:
                    return nums[mid]

        return nums[l] if nums[l]<nums[r] else nums[r]

nums = [2,0,1,1,1]
obj = Solution()
print(obj.findMin(nums))
        