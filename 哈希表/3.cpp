#include <vector>
#include <deque>
#include <string>
#include <iostream>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_map<char, int> mp;
        deque<char> queue;
        int ans = 0;
        int length;
        char ss;
        for (int i = 0; i < s.size(); i++)
        {
            queue.push_back(s[i]);
            if (mp[s[i]])
                mp[s[i]]++;
            else
                mp[s[i]] = 1;
            while (mp[s[i]]>1)
            {
                ss = queue.front();
                queue.pop_front();
                mp[ss]--;
            }
            length = queue.size();
            ans = length >= ans ? length : ans;
    
        }
        return ans;
    }
};

int main()
{
    string s = "";
    Solution obj;
    int ans = obj.lengthOfLongestSubstring(s);
    cout << ans << endl;
}