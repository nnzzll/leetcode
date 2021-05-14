#include <vector>
using namespace std;
class Solution
{
public:
    vector<int> singleNumbers(vector<int> &nums)
    {
        int x = 0, y = 0, m = 1, n = 0;
        for (auto num : nums)
            n = n ^ num;
        while ((n & m) == 0) //C++中==优先度高于逻辑运算
            m = m << 1;
        for (auto num : nums){
            if((num&m)==0)
                x = x^num;
            else
                y = y^num;
        return {x,y}; //不使用vector可以减少时间和空间
        }
    }
};