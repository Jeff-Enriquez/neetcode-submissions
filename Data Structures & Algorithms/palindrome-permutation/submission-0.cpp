class Solution {
public:
    bool canPermutePalindrome(string s) {
        int16_t counts[26] = {};
        for(char& c : s) {
            counts[c - 'a']++;
        }
        bool can_be_odd = s.length() % 2 == 1;
        for(int16_t& count : counts) {
            if(count % 2 == 1) {
                if(can_be_odd) {
                    can_be_odd = false;
                }
                else {
                    return false;
                }
            }
        }
        return true;
    }
};
