'''
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
'''
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))
        while(l<=r):
            if(l**2+r**2)<c:
                l+=1
            elif(l**2+r**2)>c:
                r -=1
            else:
                return True
        return False

c = 1000000000
obj = Solution()
print(obj.judgeSquareSum(c))