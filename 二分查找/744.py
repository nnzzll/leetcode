'''
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
在比较时，字母是依序循环出现的。举个例子：
如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
'''


class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        if target>=letters[-1]:
            return letters[0]
        l = 0
        r = len(letters)-1
        while(l<r):
            mid = l+(r-l)//2
            if letters[mid]<=target:
                l = mid+1
            else:
                r = mid
        return letters[l]

letters = ["c", "f", "j"]
target = "c"
obj = Solution()
print(obj.nextGreatestLetter(letters,target))