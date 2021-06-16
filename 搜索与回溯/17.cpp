#include<vector>
#include<string>
#include<unordered_map>
#include<iostream>
using namespace std;
class Solution {
public:
    unordered_map<char,string>mp={
              {'2',"abc"},
              {'3',"def"},
              {'4',"ghi"},
              {'5',"jkl"},
              {'6',"mno"},
              {'7',"pqrs"},
              {'8',"tuv"},
              {'9',"wxyz"}};
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if (digits.empty())
            return res;
        string combination;
        backtrack(0,digits,res,combination);
        return res;
    }

    void backtrack(int index,string&digits,vector<string>&res,string& combination){
        if(index==digits.size())
            res.push_back(combination);
        else{
            for(auto letter:mp[digits[index]]){
                combination.push_back(letter);
                backtrack(index+1,digits,res,combination);
                combination.pop_back();
            }
        }
    }
};

int main()
{
    string digits = "";
    Solution obj;
    vector<string>res = obj.letterCombinations(digits);
    for(auto s:res)
        cout<<s<<endl;
}