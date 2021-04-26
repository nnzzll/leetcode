#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int findMin(vector<int> &nums)
    {
        int l = 0;
        int r = nums.size() - 1;
        int mid;
        while (l + 1 < r)
        {
            mid = l + (r - l) / 2;
            if (nums[mid] > nums[r])
                l = mid + 1;
            else if (nums[mid] < nums[r])
                r = mid;
            else
            {
                if (nums[mid] > nums[l])
                    return nums[l];
                else if (nums[mid] == nums[l])
                {
                    l++;
                    r--;
                }
                else
                {
                    if (nums[mid] >= nums[mid - 1])
                        r = mid - 1;
                    else
                        return nums[mid];
                }
            }
        }

        return nums[l]<nums[r] ? nums[l] : nums[r];
    }
};