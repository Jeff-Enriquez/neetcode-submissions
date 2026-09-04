class Solution {
public:
    int appendCharacters(string s, string t) {
        size_t sIdx = 0;
        size_t tIdx = 0;
        while(sIdx < s.length() && tIdx < t.length()) {
            if(s[sIdx] == t[tIdx]) {
                tIdx++;
            }
            sIdx++;
        }
        return t.length() - tIdx;
    }
};