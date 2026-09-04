class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        std::map<int, int, std::greater<int>> num_map;
        for(size_t i = 0; i < arr.size(); ++i) {
            num_map[arr[i]] = i;
        }
        auto it = num_map.begin(); 
        for(size_t i = 0; i < arr.size() - 1; ++i) {
            while(it->second <= i) {
                ++it;
            }
            arr[i] = it->first;
        }
        if(arr.size() > 0) {
            arr[arr.size()-1] = -1;
        }
        return arr;
    }
};