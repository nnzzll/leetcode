'''
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
进阶：不要 使用任何内置的库函数，如  sqrt 。
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        n = num//2
        l = 0
        r = n
        while(l<=r):
            mid = l + (r-l)//2
            if mid*mid == num:
                return True
            if mid*mid>num:
                r = mid-1
            else:
                l = mid+1
        return False

num = 24
obj = Solution()
print(obj.isPerfectSquare(num))