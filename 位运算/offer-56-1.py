from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        x, y, m, n = 0, 0, 1, 0
        for num in nums:
            n = n ^ num
        while(n & m == 0):
            m = m << 1
        for num in nums:
            if num & m == 0:
                x = x ^ num
            elif num & m != 0:
                y = y ^ num
        return [x, y]


nums = [1, 2, 10, 4, 1, 4, 3, 3]
obj = Solution()
print(obj.singleNumbers(nums))
