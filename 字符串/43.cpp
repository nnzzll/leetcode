#include<string>
#include<vector>
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

    string multiply(string num1, string num2) {
        if(num1=="0"||num2=="0")
            return "0";
        int j = num2.size()-1;
        vector<string>res;
        int c = 0;
        int result = 0;
        while(j>=0)
        {
            int i = num1.size()-1;
            string temp;
            int y = num2[j]-'0';
            while(i>=0 || c!=0)
            {
                int x = i>=0? num1[i]-'0':0;
                result = x*y+c;
                temp.push_back('0'+result%10);
                c = result/10;
                i--;
            }
            reverse(temp.begin(),temp.end());
            for(int n=0;n<num2.size()-1-j;n++)
                temp.push_back('0');
            res.push_back(temp);
            j-=1;
        }
        string ans = "0";
        for(auto str:res)
            ans = addStrings(ans,str);
        return ans;
    }
};