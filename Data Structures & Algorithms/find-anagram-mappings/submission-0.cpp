class Solution {
public:
    vector<int> anagramMappings(vector<int>& nums1, vector<int>& nums2) {
        std::unordered_map<int, int> num_map;
        for(size_t i = 0; i < nums2.size(); ++i) {
            num_map[nums2[i]] = i;
        }
        for(size_t i = 0; i < nums1.size(); ++i) {
            nums1[i] = num_map[nums1[i]];
        }
        return nums1;
    }
};
