class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s = x^y
        res = 0
        while(s):
            res += s&1
            s = s>>1
        return res