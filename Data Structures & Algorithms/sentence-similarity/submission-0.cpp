class Solution {
public:
    bool areSentencesSimilar(vector<string>& sentence1, vector<string>& sentence2, vector<vector<string>>& similarPairs) {
        if(sentence1.size() != sentence2.size()) {
            return false;
        }
        unordered_set<string> words;
        for(vector<string>& pairs : similarPairs) {
            if(pairs[0] > pairs[1]) {
                words.insert(pairs[0] + '#' + pairs[1]);
            }
            else {
                words.insert(pairs[1] + '#' + pairs[0]);
            }
        }
        for(size_t i = 0; i < sentence1.size(); ++i) {
            if(sentence1[i] > sentence2[i]) {
                if(!words.contains(sentence1[i] + '#' + sentence2[i])) {
                    return false;
                }
            }
            else if(sentence1[i] < sentence2[i]) {
                if(!words.contains(sentence2[i] + '#' + sentence1[i])) {
                    return false;
                }
            }
        }
        return true;
    }
};
