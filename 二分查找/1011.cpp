#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;
class Solution
{
public:
    bool check(vector<int> &weights, int D, int ans)
    {
        int cargo = 0;
        int days = 1;
        for (auto w : weights)
        {
            cargo += w;
            if (cargo > ans)
            {
                cargo = w;
                days++;
            }
        }
        return days <= D;
    }

    int shipWithinDays(vector<int> &weights, int D)
    {
        int l = *max_element(weights.begin(), weights.end());
        int r = accumulate(weights.begin(), weights.end(), 0);
        int mid;
        while (l < r)
        {
            mid = l+(r-l)/2;
            if(check(weights,D,mid))
                r = mid;
            else
                l = mid+1;
        }
        return l;
    }
};