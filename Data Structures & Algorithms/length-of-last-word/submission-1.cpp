class Solution {
public:
    int lengthOfLastWord(string s) {
        int count = 0;
        size_t i = s.length() - 1;
        while(s[i] == ' ' && i >= 0) {
            --i;
        }
        while(s[i] != ' ' && i > 0) {
            --i;
            ++count;
        }
        if(s[i] != ' ') {
            ++count;
        }
        return count;
    }
};