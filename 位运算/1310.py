from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        '''暴力法O(nm)超时,采用前缀数组'''
        xor = [0]
        for a in arr:
            xor.append(xor[-1]^a)

        res = []
        for l,r in queries:
            res.append(xor[l]^xor[r+1])
        return res


arr =  [4,8,2,10]
queries = [[2,3],[1,3],[0,0],[0,3]]
obj = Solution()
obj.xorQueries(arr,queries)