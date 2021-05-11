#include<vector>
using namespace std;


class Solution {
public:
    vector<int> decode(vector<int>& encoded) {
        int total,odd;
        int n = encoded.size()+1;
        total = 0;
        for(int i=1;i<n+1;i++)
            total = total^i;
        odd = 0;
        for(int i=1;i<n-1;i+=2)
            odd = odd^encoded[i];
        vector<int>res;
        res.push_back(total^odd);
        for(int i=0;i<n-1;i++)
            res.push_back(res.back()^encoded[i]);
        return res;
    }
};