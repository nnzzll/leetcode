from typing import List
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''O(n^3)'''
        length = len(points)
        if length < 3:
            return length
        ans = 2
        for i in range(length):
            for j in range(i+1,length):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                temp = 2
                for k in range(j,length):
                    if (y2-y1)*(points[k][0]-x1)==(x2-x1)*(points[k][1]-y1):
                        temp += 1
                ans = max(ans,temp)
        return ans

    def _maxPoints(self,points:List[List[int]]) -> int:
        '''对每一个点，统计经过该点的斜率数量,O(N^2)'''
        length = len(points)
        if length < 3:
            return length
        ans = 2
        for i in range(length):
            mp = {}
            for j in range(length):
                if i!=j:
                    dx = points[i][0]-points[j][0]
                    dy = points[i][1]-points[j][1]
                    if dx == 0:
                        gradient = math.inf
                    else:
                        gradient = dy/dx
                    if gradient in mp:
                        mp[gradient]+=1
                    else:
                        mp[gradient] = 2
                    ans = max(ans,mp[gradient])
        return ans

points = [[1,1],[2,2],[3,3]]
obj = Solution()
print(obj._maxPoints(points))