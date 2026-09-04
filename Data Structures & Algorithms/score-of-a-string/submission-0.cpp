class Solution {
public:
    int scoreOfString(string s) {
        int sum = 0;
        for(size_t i = 1; i < s.size(); ++i) {
            sum += std::abs(s[i] - s[i - 1]);
        }
        return sum;
    }
};