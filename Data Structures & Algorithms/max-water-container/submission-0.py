class Solution:
    """A class to solve the container with most water problem."""

    def maxArea(self, heights: list[int]) -> int:
        """Calculate the maximum area of water that can be contained.

        Args:
            heights: A list of integers representing the heights of the lines.

        Returns:
            The maximum area of water that can be contained.
        """
        max_area: int = 0
        left_ptr: int = 0
        right_ptr: int = len(heights) - 1

        while left_ptr < right_ptr:
            max_area = max(
                max_area,
                min(heights[left_ptr], heights[right_ptr]) * (right_ptr - left_ptr)
            )
            if heights[left_ptr] < heights[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        return max_area
