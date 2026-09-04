class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> num_idx;
        for(size_t i = 0; i < nums.size(); i++) {
            if(num_idx.contains(target - nums[i])) {
                return {num_idx.find(target - nums[i])->second, i};
            }
            num_idx.emplace(nums[i], i);
        }
        return {-1, -1};
    }
};
