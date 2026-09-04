class StringIterator {
public:
    string s;
    uint16_t idx = 0;
    char currChar;
    uint16_t currCount;
    StringIterator(string compressedString) : s(compressedString) {
        currChar = s[idx++];
        uint16_t rPtr = idx;
        while(s[rPtr] >= '0' && s[rPtr] <= '9') {
            ++rPtr;
        }
        currCount = static_cast<uint16_t>(stoi(s.substr(idx, rPtr - idx)));
        idx = rPtr;
    }
    
    char next() {
        if(currCount > 0) {
            --currCount;
            return currChar;
        }
        currChar = s[idx++];
        uint16_t rPtr = idx;
        while(s[rPtr] >= '0' && s[rPtr] <= '9') {
            ++rPtr;
        }
        currCount = static_cast<uint16_t>(stoi(s.substr(idx, rPtr - idx))) - 1;
        idx = rPtr;
        return currChar;
    }
    
    bool hasNext() {
        if(idx == s.length()) {
            return currCount > 0;
        } else {
            return true;
        }
    }
};

/**
 * Your StringIterator object will be instantiated and called as such:
 * StringIterator* obj = new StringIterator(compressedString);
 * char param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
