#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int findMin(vector<int> &nums)
    {
        int l = 0;
        int r = nums.size() - 1;
        int mid;
        while (l < r)
        {
            mid = l + (r - l) / 2;
            if (nums[mid] > nums[r])
                l = mid + 1;
            if (nums[mid] <= nums[r])
                r = mid;
        }
        return nums[l];
    }
};