class Solution {
public:
    string stringShift(string s, vector<vector<int>>& shift) {
        int16_t total_amount = 0;
        for(auto& dir_amt : shift) {
            if(dir_amt[0] == 0) {
                total_amount -= dir_amt[1];
            }
            else {
                total_amount += dir_amt[1];
            }
        }
        // Reduce to lowest common denominator
        total_amount %= int16_t(s.length());
        // No change needed
        if(total_amount == 0) {
            return s;
        }
        cout << total_amount;
        // Change left shift to equivalent right shift
        if(total_amount < 0) {
            total_amount = s.length() + total_amount;
        }
        // Perform right shift
        // Reverse the entire array
        uint8_t lPtr = 0;
        uint8_t rPtr = s.length() - 1;
        char tempC;
        while(lPtr < rPtr) {
            tempC = s[lPtr];
            s[lPtr] = s[rPtr];
            s[rPtr] = tempC;
            ++lPtr;
            --rPtr;
        }
        // Reverse the first section
        lPtr = 0;
        rPtr = total_amount - 1;
        while(lPtr < rPtr) {
            tempC = s[lPtr];
            s[lPtr] = s[rPtr];
            s[rPtr] = tempC;
            ++lPtr;
            --rPtr;
        }
        // Reverse the second section
        lPtr = total_amount;
        rPtr = s.length() - 1;
        while(lPtr < rPtr) {
            tempC = s[lPtr];
            s[lPtr] = s[rPtr];
            s[rPtr] = tempC;
            ++lPtr;
            --rPtr;
        }
        return s;
    }
};
