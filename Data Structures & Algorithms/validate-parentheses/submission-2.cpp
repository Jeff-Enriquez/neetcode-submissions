class Solution {
public:
    bool isValid(string s) {
        int open_to_close[84];
        open_to_close['(' - 40] = ')';
        open_to_close['{' - 40] = '}';
        open_to_close['[' - 40] = ']';
        stack<char> brackets;
        for(auto& c : s) {
            if(c == '(' || c == '{' || c == '[') {
                brackets.push(c);
            }
            else if(brackets.empty() || open_to_close[brackets.top()-40] != c) {
                return false;
            }
            else {
                brackets.pop();
            }
        }
        return brackets.empty();
    }
};
