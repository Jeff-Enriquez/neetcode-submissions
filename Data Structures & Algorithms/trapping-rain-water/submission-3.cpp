class Solution {
public:
    int trap(vector<int>& height) {
        size_t l_ptr = 0;
        size_t r_ptr = height.size() - 1;
        int prefix_max_height = height[l_ptr];
        int suffix_max_height = height[r_ptr];
        int total_trapped_water = 0;
        
        while (l_ptr < r_ptr) {
            if (prefix_max_height < suffix_max_height) {
                ++l_ptr;
                total_trapped_water += max(0, min(prefix_max_height, suffix_max_height) - height[l_ptr]);
                prefix_max_height = max(prefix_max_height, height[l_ptr]);
            } else {
                --r_ptr;
                total_trapped_water += max(0, min(prefix_max_height, suffix_max_height) - height[r_ptr]);
                suffix_max_height = max(suffix_max_height, height[r_ptr]);
            }
        }

        return total_trapped_water;
    }
};
