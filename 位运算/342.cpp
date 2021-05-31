class Solution {
public:
    bool isPowerOfFour(int n) {
        int mask=0b10101010101010101010101010101010;
        return n>0 && ((n&(n-1))==0) && (n&mask)==0;
    }
};