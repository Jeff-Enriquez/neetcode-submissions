class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int maxDist = 0;
        int maxN = arrays[0][0];
        int minN = maxN;
        // Get the min and max of first array
        for(size_t i = 0; i < arrays[0].size(); ++i) {
            if(arrays[0][i] > maxN) {
                maxN = arrays[0][i];
            }
            if(arrays[0][i] < minN) {
                minN = arrays[0][i];
            }
        }
        // Check the rest
        for(size_t i = 1; i < arrays.size(); ++i) {
            int currMax = arrays[i][0];
            int currMin = currMax;
            for(auto& num : arrays[i]) {
                if(num > currMax) {
                    currMax = num;
                }
                if(num < currMin) {
                    currMin = num;
                }
            }
            maxDist = max(maxDist, max(abs(minN - currMax), abs(maxN - currMin)));
            if(currMin < minN) {
                minN = currMin;
            }
            if(currMax > maxN) {
                maxN = currMax;
            }
        }
        return maxDist;
    }
};
