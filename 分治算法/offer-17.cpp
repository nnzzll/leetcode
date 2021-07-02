#include <vector>
#include <string>
#include <iostream>
using namespace std;
class Solution
{
public:
    vector<int> res;
    vector<int> printNumbers(int n)
    {
        string num(n, '0');
        dfs(0,n,num);
        return res;
    }

    void dfs(int x, int n, string &num)
    {
        if (x == n)
        {
            int ptr = 0;
            while(ptr<n&&num[ptr]=='0') ptr++;
            if(ptr!=n)
                res.push_back(stoi(num.substr(ptr)));
            return;
        }
        for (int i=0; i < 10; i++)
        {
            num[x] = '0' + i;
            dfs(x + 1,n,num);
        }
    }
};

int main()
{
    int n = 2;
    Solution obj;
    vector<int>res = obj.printNumbers(n);
    for(auto num:res)
        cout<<num<<endl;
}