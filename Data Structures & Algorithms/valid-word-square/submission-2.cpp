class Solution {
public:
    bool validWordSquare(vector<string>& words) {
        size_t len = words[0].length();
        for(string word : words) {
            if(word.length() < len) {
                len = word.length();
            } else if(word.length() > len) {
                return false;
            }
        }
        string word;
        for(size_t row = 0; row < words.size(); ++row) {
            word = words[row];
            if(word.length() > words.size()) {
                return false;
            }
            for(size_t col = 0; col < word.length(); ++col) {
                if(word[col] != words[col][row]) {
                    return false;
                }
            }
        }
        return true;
    }
};
