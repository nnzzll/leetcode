from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        total = 0
        n = len(encoded)+1
        for i in range(1,n+1):
            total = total^i
        odd = 0
        for i in range(1,n-1,2):
            odd = odd^encoded[i]
        res = [total^odd]
        for i in range(n-1):
            res.append(res[-1]^encoded[i])
        return res

encoded = [6,5,4,6]
obj = Solution()
print(obj.decode(encoded))