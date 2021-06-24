#include<vector>
#include<unordered_map>
using namespace std;
class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int len = points.size();
        if(len < 3) {
            return len;
        }
        int maxNum = 2;
        // 遍历每两个点
        for(int i = 0; i < len; i ++) {

            unordered_map<double, int> count;
            for(int j = 0; j < len; j ++) {
                if(i != j) {
                    int dx = points[i][0] - points[j][0];
                    int dy = points[i][1] - points[j][1];
                    double gradient = dy * 1.0 / dx;
                    if(count.count(gradient)) {
                        count[gradient] ++;
                    } else {
                        count[gradient] = 2;
                    }
                    maxNum = max(maxNum, count[gradient]);
                } 
            }  
        }
        return maxNum;
    }
};

int main()
{
    vector<vector<int>> points = {{1,1},{3,2},{5,3},{4,1},{2,3},{1,4}};
    Solution obj;
    obj.maxPoints(points);
}