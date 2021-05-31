class Solution:

    def isPowerOfFour(self, n: int) -> bool:
        '''循环,时间复杂度O(c)'''
        cnt = 0
        other = 0
        if n < 0:
            return False
        for i in range(31):
            if(n>>i)&1:
                if i%2==0:
                    cnt += 1
                else:
                    other+=1
        if cnt==1 and other==0:
            return True
        else:
            return False
    
    def isPowerOfFour_(self,n):
        '''2的幂满足n&(n-1)==0,时间复杂度O(1)'''
        mask = 0b10101010101010101010101010101010
        return n>0 and (n&(n-1)==0) and (n&mask)==0
        


n = 64
obj = Solution()
print(obj.isPowerOfFour_(n))