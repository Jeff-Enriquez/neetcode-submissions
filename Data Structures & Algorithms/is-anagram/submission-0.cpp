class Solution {
public:
    bool isAnagram(string s, string t) {
        std::cout << 'z' - 0;
        int letters[57] = {};
        for(char& c : s) {
            letters[c - 65]++;
        }
        for(char& c : t) {
            letters[c - 65]--;
        }
        for(int& letter : letters) {
            if(letter != 0) {
                return false;
            }
        }
        return true;
    }
};
