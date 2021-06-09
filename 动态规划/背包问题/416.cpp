#include <vector>
using namespace std;
class Solution
{
public:
    bool canPartition(vector<int> &nums)
    {
        int Sum = 0;
        int MaxNum = 0;
        for (auto num : nums)
        {
            Sum += num;
            if (num > MaxNum)
                MaxNum = num;
        }
        if ((Sum % 2 != 0) || (MaxNum > Sum / 2) || (nums.size() < 2))
        {
            return false;
        }
        int target = Sum / 2;
        vector<vector<int>> dp(nums.size(), vector<int>(target + 1));
        dp[0][nums[0]] = 1;
        for (int i = 0; i < nums.size(); i++)
            dp[i][0] = 1;
        for (int i = 1; i < nums.size(); i++)
            for (int j = 0; j < target + 1; j++)
            {
                if(j>=nums[i])
                    dp[i][j] = dp[i-1][j]||dp[i-1][j-nums[i]];
                else
                    dp[i][j] = dp[i-1][j];
            }
        return dp[nums.size()-1][target];
    }
};