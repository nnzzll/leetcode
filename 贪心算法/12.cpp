#include<string>
#include<vector>
using namespace std;
class Solution {
public:
    string intToRoman(int num) {
        vector<int> nums = {1000,900,500,400,100,90,50,40,5,4,1};
        vector<string> roman = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        string res;
        for(int i=0;i<13;i++)
            while(num/nums[i]>0)
            {
                num -= nums[i];
                res += roman[i];
            }
        return res;
    }
};