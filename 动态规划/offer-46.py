class Solution:
    def translateNum(self, num: int) -> int:
        a = 1
        b = 1
        y = num%10
        while(num>9):
            num //= 10
            x = num%10
            temp = b if 10<=x*10+y<26 else 0
            c = a+temp
            b = a
            a = c
            y = x
        return a

num = 12258
obj = Solution()
print(obj.translateNum(num))