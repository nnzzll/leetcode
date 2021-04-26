#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int findPeakElement(vector<int> &nums)
    {
        int l = 0;
        int r = nums.size() - 1;
        int mid;
        while (l < r)
        {
            mid = l + (r - l) / 2;
            if (nums[mid] > nums[mid + 1])
                r = mid;
            else if (nums[mid] < nums[mid + 1])
                l = mid + 1;
        }
        return l;
    }
};

int main(){
    vector<int> nums = {1,2,3,4,2};
    Solution obj;
    cout<<obj.findPeakElement(nums)<<endl;
}