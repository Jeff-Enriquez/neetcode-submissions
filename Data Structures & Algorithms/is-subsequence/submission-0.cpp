class Solution {
public:
    bool isSubsequence(string s, string t) {
        size_t sIdx = 0;
        for(size_t tIdx = 0; tIdx < t.length() && sIdx != s.length(); ++tIdx) {
            if(t[tIdx] == s[sIdx]) {
                sIdx++;
            }
        }
        return sIdx == s.length();
    }
};