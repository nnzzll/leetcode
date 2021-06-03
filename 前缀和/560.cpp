#include <vector>
#include <unordered_map>
using namespace std;
class Solution
{
public:
    int subarraySum(vector<int> &nums, int k)
    {
        int prefix = 0;
        int count = 0;
        unordered_map<int, int> dic;
        dic[0] = 1;
        for (auto num : nums)
        {
            prefix += num;
            if (dic.count(prefix - k))
                count += dic[prefix-k];
            dic[prefix]++;
        }
        return count;
    }
};