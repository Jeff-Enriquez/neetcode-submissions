class Solution:
    """Class to solve the water trapping problem."""

    def trap(self, height: list[int]) -> int:
        """Calculate the total amount of trapped rainwater given the elevation map.

        Args:
            height: A list of non-negative integers representing the elevation map.

        Returns:
            The total amount of trapped rainwater.
        """
        height_length: int = len(height)
        prefix_max: list[int] = []
        suffix_max: int = 0
        total_trapped_water: int = 0

        prefix_max.append(height[0])
        for i in range(1, height_length):
            prefix_max.append(max(height[i], prefix_max[i - 1]))

        for i in range(height_length - 1, -1, -1):
            suffix_max = max(suffix_max, height[i])
            total_trapped_water += min(prefix_max[i], suffix_max) - height[i]

        return total_trapped_water
