#include <vector>
using namespace std;
class Solution
{
public:
    int count = 0;
    int findTargetSumWays(vector<int> &nums, int target)
    {
        dfs(nums, 0, 0, target);
        return count;
    }

    void dfs(vector<int> &nums, int idx, int Sum, int target)
    {
        if (idx == nums.size())
        {
            if (Sum == target)
            {
                count++;
            }
        }
        else
        {
            dfs(nums, idx + 1, Sum + nums[idx], target);
            dfs(nums, idx + 1, Sum - nums[idx], target);
        }
    }
};