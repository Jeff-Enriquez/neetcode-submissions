class Solution {
public:
    int calculateTime(string keyboard, string word) {
        // 97 is the starting letter
        int8_t indexes[26] = {};
        for(int8_t i = 0; i < 26; ++i) {
            indexes[keyboard[i] - 'a'] = i;
        }
        int time = indexes[word[0] - 'a'];
        for(size_t i = 1; i < word.length(); ++i) {
            time += abs(indexes[word[i] - 'a'] - indexes[word[i - 1] - 'a']);
        }
        return time;
    }
};
