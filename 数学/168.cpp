#include<string>
#include<iostream>
#include<algorithm>
using namespace std;
class Solution {
public:
    string convertToTitle(int columnNumber) {
        string ans;
        int mod;
        while(columnNumber>0){
            mod = columnNumber%26;
            if(mod){
                ans.push_back('A'+(mod-1));
                columnNumber/=26;
            }
            else{
                ans.push_back('Z');
                columnNumber/=26;
                columnNumber--;
            }
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};

int main()
{
    int columnNumber=52;
    Solution obj;
    cout<<obj.convertToTitle(columnNumber)<<endl;
}