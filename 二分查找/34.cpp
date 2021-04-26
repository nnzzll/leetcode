#include <vector>
using namespace std;
class Solution
{
private:
    int binarySearch(vector<int>&nums ,int target){
        int l=0;
        int h=nums.size()-1;
        int idx = -1;
        while(l<=h){
            idx = int((l+h)/2);
            if(nums[idx]>target){
                h = idx-1;
            }
            else if(nums[idx]<target){
                l = idx+1;
            }
            else{
                return idx; 
            }
        }
        return -1;
    }
public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        int anchor = binarySearch(nums,target);
        if(anchor==-1) return {-1,-1};
        vector<int> res;
        int first = anchor;
        while((first>0)&&(nums[first-1]==target)) first--;
        res.push_back(first);
        int second = anchor;
        while(((second)<nums.size()-1)&&(nums[second+1]==target)) second++;
        res.push_back(second);
        return res;
    }
};