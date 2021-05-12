#include<vector>
using namespace std;
class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int>xor;
        xor.push_back(0);
        for(auto a:arr)
            xor.push_back(xor.back()^a);
        vector<int>res;
        for(auto &q:queries)
            res.push_back(xor[q[0]]^xor[q[1]+1]);
        return res;
    }
};