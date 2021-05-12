#include<vector>
using namespace std;
class Solution {
public:
    vector<int> xor_arrQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int>xor_arr;
        xor_arr.push_back(0);
        for(auto a:arr)
            xor_arr.push_back(xor_arr.back()^a);
        vector<int>res;
        for(auto &q:queries)
            res.push_back(xor_arr[q[0]]^xor_arr[q[1]+1]);
        return res;
    }
};