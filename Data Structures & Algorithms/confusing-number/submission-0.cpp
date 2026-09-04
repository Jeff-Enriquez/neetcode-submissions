class Solution {
public:
    bool confusingNumber(int n) {
        string s = to_string(n);
        // catch edge case
        if(s.length() == 1) {
            return n == 6 || n == 9;
        }
        // check if any numbers are invalid
        for(char& num : s) {
            if(num == '2' || num == '3' || num == '4' || num == '5' || num == '7') {
                return false;
            }
        }
        const char* num_arr = s.data();
        // at this point, if it ends in zero it will alwsy be a "confusing number"
        if(num_arr[s.length() - 1] == '0') {
            return true;
        }
        // check if it is a "confusing number" after rotating 180 degrees
        size_t lPtr = 0;
        size_t rPtr = s.length() - 1;
        while(lPtr < rPtr) {
            if(num_arr[lPtr] != num_arr[rPtr] && !(
                (num_arr[lPtr] == '6' && num_arr[rPtr] == '9') ||
                (num_arr[lPtr] == '9' && num_arr[rPtr] == '6')
            )) {
                return true;
            }
            ++lPtr;
            --rPtr;
        }
        return false;
    }
};
