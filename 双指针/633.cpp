#include <cmath>
class Solution
{
public:
    bool judgeSquareSum(int c)
    {
        long l = 0;
        long r = sqrt(c);
        while (l <= r)
        {
            if ((l * l + r * r) < c)
                l++;
            else if ((l * l + r * r) > c)
                r--;
            else
                return true;
        }
        return false;
    }
};