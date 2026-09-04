class Solution {
public:
    int largestUniqueNumber(vector<int>& nums) {
        int arr_nums[1001] = {};
        for(int& num : nums) {
            arr_nums[num]++;
        }
        int largestUniqueNumber = -1;
        for(size_t i = 1; i < 1001; ++i) {
            if(arr_nums[i] == 1) {
                largestUniqueNumber = i;
            }
        }
        return largestUniqueNumber;
    }
};
