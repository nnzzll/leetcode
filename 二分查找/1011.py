class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        l = max(weights)
        r = sum(weights)
        while(l < r):
            mid = l+(r-l)//2
            if(self.check(weights, D, mid)):
                r = mid
            else:
                l = mid+1
        return l

    def check(self, weights, D, ans):
        cargo = 0
        days = 1
        for w in weights:
            cargo += w
            if(cargo > ans):
                cargo = w
                days += 1
        return days <= D


weights = [1,2,3,4,5,6,7,8,9,10]
obj = Solution()
print(obj.shipWithinDays(weights,5))