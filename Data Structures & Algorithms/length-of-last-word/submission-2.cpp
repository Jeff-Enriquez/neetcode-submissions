class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = 0;
        size_t rPtr = s.length() - 1;
        while(s[rPtr] == ' ' && rPtr > 0) {
            --rPtr;
        }
        while(s[rPtr] != ' ' && rPtr > 0) {
            ++len;
            --rPtr;
        }
        if(s[rPtr] != ' ') {
            ++len;
        }
        return len;
    }
};