#include<vector>
using namespace std;
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i = nums.size()-2;
        while(i>=0 && nums[i]>=nums[i+1])
            i--;
        if(i>=0){
            int j = nums.size()-1;
            while(i<j && nums[i]>=nums[j])
                j--;
            int temp = nums[j];
            nums[j] = nums[i];
            nums[i] = temp;
        }
        reverse(nums.begin()+i+1,nums.end());
    }
};