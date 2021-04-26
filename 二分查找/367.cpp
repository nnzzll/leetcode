class Solution
{
public:
    bool isPerfectSquare(int num)
    {
        if (num == 1)
            return true;
        int n = num / 2;
        int l = 0;
        int r = n;
        int mid;
        while (l <= r)
        {
            mid = l + (r - l) / 2;
            if (mid * mid == num)
                return true;
            if (mid * mid > num)
                r = mid - 1;
            else
                l = mid + 1;
        }
        return false;
    }
};