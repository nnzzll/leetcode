'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数，即x^n）。
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n % 2 == 0:
            if n > 0:
                return self.myPow(x, n/2)*self.myPow(x, n/2)
            else:
                return 1/(self.myPow(x, -n/2)*self.myPow(x, -n/2))
        if n % 2 == 1:
            if n > 0:
                return self.myPow(x, n-1)*x
            else:
                return 1/(self.myPow(x, -n-1)*x)

    def _myPow(self, x: float, n: int) -> float:
        ans = 1
        abs_n = abs(n)
        while(abs_n):
            if abs_n%2==1:
                ans = ans * x
            x = x*x
            abs_n = abs_n//2
        return ans if n>=0 else 1/ans

x = 2
n = -4
obj = Solution()
print(obj._myPow(x, n))
