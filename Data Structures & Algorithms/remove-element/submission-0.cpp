class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        size_t l_idx = 0;
        for(size_t i = 0; i < nums.size(); i++) {
            if(nums[i] != val) {
                nums[l_idx++] = nums[i];
            }
        }
        return l_idx;
    }
};