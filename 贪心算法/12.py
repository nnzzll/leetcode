class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        res = []
        for key in dic.keys():
            while(num//key>0):
                res.append(dic[key])
                num -= key
        return "".join(res)

num = 2984
obj = Solution()
print(obj.intToRoman(num))