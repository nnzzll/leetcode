from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        dic = {0:-1}
        mod = 0
        for i in range(len(nums)):
            mod = (mod+nums[i])%k
            idx = dic.get(mod)
            if idx is not None:
                if (i-idx)>=2:
                    return True
                else:
                    continue
            dic[mod] = i
        return False


nums=[23,24,7,6]
k=31
obj=Solution()
print(obj.checkSubarraySum(nums, k))
