class Solution {
public:
    int hammingDistance(int x, int y) {
        int s = x^y;
        int res = 0;
        while(s){
            res += s&1;
            s = s>>1;
        }
        return res;
    }
};