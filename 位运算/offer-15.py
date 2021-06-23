class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n>0:
            count += n&1
            n = n>>1
        return count

n = 0b00000000000000000000000010000000
obj = Solution()
print(obj.hammingWeight(n))