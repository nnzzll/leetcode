#include<string>
using namespace std;


class Solution {
public:
    string addStrings(string num1, string num2) {
        int i=num1.size()-1;
        int j=num2.size()-1;
        string res;
        int c = 0;
        int add = 0;
        while(i>=0 || j>=0 || c!=0)
        {
            int x = i>=0? num1[i]-'0':0;
            int y = j>=0? num2[j]-'0':0;
            add = x+y+c;
            res.push_back('0'+add%10);
            c = add/10;
            i--;
            j--;
        }
        reverse(res.begin(),res.end());
        return res;
    }
};