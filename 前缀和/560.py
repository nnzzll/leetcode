from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        dic = {0: 1}
        for num in nums:
            prefix += num
            if dic.get(prefix-k) is not None:
                count += dic[prefix-k]
            if dic.get(prefix) is None:
                dic[prefix] = 0
            dic[prefix] += 1
        return count


nums = [1, -1, 0]
k = 0
obj = Solution()
print(obj.subarraySum(nums, k))
# obj.subarraySum(nums, k)
