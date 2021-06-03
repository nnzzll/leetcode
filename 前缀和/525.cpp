#include <vector>
#include <unordered_map>
using namespace std;
class Solution
{
public:
    int findMaxLength(vector<int> &nums)
    {
        unordered_map<int,int>mp;
        mp[0] = -1;
        int max_length=0;
        int count = 0;
        for(int i =0;i<nums.size();i++){
            if(nums[i])
                count++;
            else
                count--;
            if(mp.count(count))
                max_length = i-mp[count]>max_length? i-mp[count]:max_length;
            else
                mp[count] = i;
        }
        return max_length;
    }
};