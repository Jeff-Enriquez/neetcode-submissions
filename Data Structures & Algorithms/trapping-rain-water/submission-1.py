class Solution:
    def trap(self, height: list[int]) -> int:
        # Water equals sum of height[i] where min(l,r) - h[i]
        l_ptr: int = 0
        r_ptr: int = len(height) - 1
        max_left: int = height[l_ptr]
        max_right: int = height[r_ptr]
        total_water: int = 0
        
        while (l_ptr < r_ptr):
            if (max_left < max_right):
                l_ptr += 1
                total_water += max(0, min(max_left, max_right) - height[l_ptr])
                max_left = max(max_left, height[l_ptr])
            else:
                r_ptr -= 1
                total_water += max(0, min(max_left, max_right) - height[r_ptr])
                max_right = max(max_right, height[r_ptr])
        
        return total_water
