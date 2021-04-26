#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    char nextGreatestLetter(vector<char> &letters, char target)
    {
        if (letters.back()<= target)
            return letters[0];
        int l = 0;
        int r = letters.size() - 1;
        int mid;
        while (l < r)
        {
            mid = l + (r - l) / 2;
            if (letters[mid] <= target)
                l = mid + 1;
            else
                r = mid;
        }
        return letters[l];
    }
};

int main(){
    vector<char> letters = {'c', 'f', 'j'};
    char target = 'c';
    Solution obj;
    cout<<obj.nextGreatestLetter(letters,target)<<endl;
}