from typing import List 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        mp = {'2':"abc",
              '3':"def",
              '4':"ghi",
              '5':"jkl",
              '6':"mno",
              '7':"pqrs",
              '8':"tuv",
              '9':"wxyz",}
        combination = []
        res = []
        def backtrack(index):
            if index==len(digits):
                res.append("".join(combination))
            else:
                for letter in mp[digits[index]]:
                    combination.append(letter)
                    backtrack(index+1)
                    combination.pop()
        backtrack(0)
        return res

digits =""
obj = Solution()
print(obj.letterCombinations(digits))