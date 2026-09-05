"""Module to find the longest consecutive sequence in a list of integers.

This module provides a class `Solution` with a method `longest_consecutive` that
finds the length of the longest consecutive sequence in a list of integers.
"""

from collections.abc import Mapping

class Solution:
    """Class to find the longest consecutive sequence in a list of integers."""

    def longestConsecutive(self, nums: list[int]) -> int:
        """Finds the length of the longest consecutive sequence in a list of integers.

        Args:
            nums: A list of integers.

        Returns:
            The length of the longest consecutive sequence.
        """
        num_map: Mapping[int, int] = {}
        longest_streak = 0

        for num in nums:
            if num not in num_map:
                # Length of previous number + length of current number + 1 (number we are adding to the length)
                length = num_map.get(num - 1, 0) + num_map.get(num + 1, 0) + 1
                num_map[num] = length

                # Update left boundary
                left_boundary = num - num_map.get(num - 1, 0)
                num_map[left_boundary] = length

                # Update right boundary
                right_boundary = num + num_map.get(num + 1, 0)
                num_map[right_boundary] = length

                longest_streak = max(longest_streak, length)

        return longest_streak
