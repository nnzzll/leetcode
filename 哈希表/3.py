from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            queue = deque()
            dic = {}
            res = [0 for _ in range(len(s))]
            for i in range(len(s)):
                queue.append(s[i])
                if s[i] not in dic:
                    dic[s[i]] = 1
                else:
                    dic[s[i]]+=1

                while(dic[s[i]]>1):
                    ss = queue.popleft()
                    dic[ss] -= 1
                res[i] = len(queue)
            return max(res)
        else:
            return 0
            

s = ""
obj = Solution()
print(obj.lengthOfLongestSubstring(s))
