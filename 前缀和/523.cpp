#include<vector>
#include<unordered_map>
using namespace std;
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        if(nums.size()<2)
            return false;
        unordered_map<int,int>dict;
        dict[0] = -1;
        int mod = 0;
        for(int i=0;i<nums.size();i++){
            mod += nums[i];
            mod = mod%k;
            if(dict.find(mod)!=dict.end()){
                if((i-dict[mod])>=2)
                    return true;
            }
            else
                dict[mod] = i;
        }
        return false;
    }
};