#include<vector>
#include<algorithm>
#include<iostream>
#include<numeric>
using namespace std;
class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        long long right = accumulate(nums.begin(),nums.end(),0);
        long long left = *max_element(nums.begin(),nums.end());
        while(left<right){
            long long mid = left+(right-left)/2;
            if(check(nums,mid,m))
                right = mid;
            else
                left = mid+1;
        }
        return left;
    }

    bool check(vector<int>&nums,int temp, int m)
    {
        int _temp_sum = 0;
        int cnt = 1;
        for(int i=0;i<nums.size();i++){
            if(_temp_sum+nums[i]>temp){
                cnt++;
                _temp_sum=nums[i];
            }
            else
                _temp_sum += nums[i];
        }
        return cnt<=m;
    }
};