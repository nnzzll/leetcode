class Solution:
    def decode(self, encoded, first: int):
        res = [first]
        pre = first
        for num in encoded:
            ans = pre^num
            res.append(ans)
            pre = ans
        return res

encoded = [1,2,3]
first = 1
obj = Solution()
print(obj.decode(encoded,first))