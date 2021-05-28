#include<vector>
using namespace std;
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int res = 0;
        int n = nums.size();
        for(int i =0;i<30;i++){
            int c = 0;
            for(auto val:nums)
                c += (val>>i)&1;
            res += c*(n-c);
        }
        return res;
    }
};