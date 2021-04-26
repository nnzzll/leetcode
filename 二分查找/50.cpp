#include <iostream>
using namespace std;

class Solution
{
public:
    //迭代快速幂 O(logn),O(logn)
    double qPow(double x, long long N)
    {
        if (N == 0)
            return 1;
        double temp = qPow(x, N / 2);
        return N % 2 == 0 ? temp * temp : temp * temp * x;
    }
    //非迭代快速幂 O(logn),O(1)
    double loopPow(double x, long long N)
    {
        double res = 1;
        while (N)
        {
            if (N % 2 == 1)
                res = res * x;
            x = x * x;
            N = N / 2;
        }
        return res;
    }
    double myPow(double x, int n)
    {
        long long N = n;
        return N >= 0 ? loopPow(x, N) : 1 / loopPow(x, -N);
    }
};

int main()
{
    double x = 2;
    int n = -3;
    Solution obj;
    cout << obj.myPow(x, n) << endl;
}