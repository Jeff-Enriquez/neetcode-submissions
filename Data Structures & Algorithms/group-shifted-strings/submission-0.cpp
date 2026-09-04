class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        unordered_map<string, vector<string>> buckets;
        string temp;
        for(auto& s : strings) {
            temp = "";
            for(size_t i = 0; i < s.length() - 1; ++i) {
                temp.append(
                    to_string(
                        (static_cast<int>(s[i] - s[i + 1]) + 26) % 26
                        ));
                temp.append("#");
            }
            if(!buckets.contains(temp)) {
                buckets.emplace(temp, vector<string>{});
            }
            buckets.find(temp)->second.push_back(s);
        }
        vector<vector<string>> ans;
        for(auto& [key, value] : buckets) {
            ans.push_back(value);
        }
        return ans;
    }
};
