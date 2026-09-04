class Solution {
public:
    int countElements(vector<int>& arr) {
        unordered_map<uint16_t, uint16_t> arr_map;
        pair<std::unordered_map<uint16_t, uint16_t>::iterator, bool> res;
        for(auto& num : arr) {
            // initialize key with value of 1
            res = arr_map.try_emplace(num, 1);
            // key already exists
            if(!res.second) {
                // increment value
                res.first->second++;
            }
        }
        int count = 0;
        for(const auto& [key, value] : arr_map) {
            if(arr_map.contains(key + 1)) {
                count += value;
            }
        }
        return count;
    }
};
