class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> temp = {};
        temp.push_back(nums[0]);
        for(size_t i = 1; i < nums.size(); i++) {
            if(temp[temp.size()-1] != nums[i]) {
                temp.push_back(nums[i]);
            }
        }
        nums.assign(temp.begin(), temp.end());
        return temp.size();
    }
};