class Solution {
    public int climbStairs(int n) {
        int prev2 = 2;
        int prev1 = 3;
        int curr = n;
        for(int i = 3; i < n; i++) {
            curr = prev2 + prev1;
            prev2 = prev1;
            prev1 = curr;
        }
        return curr;
    }
}
