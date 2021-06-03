from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 逢1加1,逢0减1
        count = 0
        dic = {0:-1}
        max_length = 0
        for i in range(len(nums)):
            count = count+1 if nums[i] else count-1
            if dic.get(count) is not None:
                max_length = i-dic[count] if i-dic[count]>max_length else max_length
            else:
                dic[count] = i
        return max_length

nums = [0,1,0,1,1,1,0]
obj = Solution()
print(obj.findMaxLength(nums))
