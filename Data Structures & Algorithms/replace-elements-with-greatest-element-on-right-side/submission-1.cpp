class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int maxRight = -1;
        for(size_t i = arr.size() - 1; i > 0; --i) {
            int temp = arr[i];
            arr[i] = maxRight;
            maxRight = max(temp, maxRight);
        }
        arr[0] = maxRight;
        return arr;
    }
};