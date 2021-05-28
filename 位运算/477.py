from typing import List
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(30):
            c = 0 # 第i位为1的元素数量
            for num in nums:
                c += (num>>i)&1
            res += c*(n-c)
        return res

nums = [4,14,2]
obj = Solution()
print(obj.totalHammingDistance(nums))