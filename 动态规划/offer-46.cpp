class Solution {
public:
    int translateNum(int num) {
        int a,b,c,x,y,temp;
        y = num%10;
        a = 1;
        b = 1;
        while(num>9){
            num = num/10;
            x = num%10;
            if((x*10+y)>9 &&(x*10+y)<26)
                temp = b;
            else
                temp = 0;
            c = a+temp;
            b = a;
            a = c;
            y = x;
        }
        return a;
    }
};