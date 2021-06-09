#include<vector>
using namespace std;
class Solution {
public:
    int findTargetSumWays(vector<int> &nums, int target)
    {
        int Sum = 0;
        for(auto num:nums)
            Sum += num;
        if(((Sum-target)<0)||(Sum-target)%2!=0)
            return 0;
        int total = (Sum-target)/2;
        vector<vector<int>>dp(nums.size()+1,vector<int>(total+1));
        dp[0][0] = 1;
        for(int i=1;i<nums.size()+1;i++){
            int num = nums[i-1];
            for(int j=0;j<total+1;j++){
                dp[i][j] = dp[i-1][j];
                if(j>=num)
                    dp[i][j]+=dp[i-1][j-num];
            }
        }
        return dp[nums.size()][total];
    }
};