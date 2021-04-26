'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
'''


class Solution:
    def find(self, arr, target):
        l = 0
        h = len(arr)-1
        while(l <= h):
            idx = (l+h)//2
            if(arr[idx] > target):
                h = idx-1
            elif(arr[idx] < target):
                l = idx+1
            else:
                return idx
        return -1

    def searchRange(self, nums, target):
        anchor = self.find(nums, target)
        if anchor == -1:
            return [-1, -1]
        res = []
        idx = anchor

        while (idx > 0) and (nums[idx-1] == target):
            idx -= 1
        res.append(idx)

        idx = anchor

        while (idx < len(nums)-1) and (nums[idx+1] == target):
            idx += 1
        res.append(idx)
        return res


arr = [1,4]
obj = Solution()
res = obj.searchRange(arr, 4)
print(res)
