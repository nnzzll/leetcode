#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    int cuttingRope(int n) {
        if(n<=3)
            return n-1;
        vector<int>dp(n+1);
        dp[2] = 1;
        for(int i=4;i<=n;i++)
            for(int j=2;j<i;j++)
                dp[i] = max(dp[i],max(j*(i-j),j*dp[i-j]));
        return dp[n];
    }
};

int main()
{
    int n = 10;
    Solution obj;
    cout<<obj.cuttingRope(n)<<endl;
}