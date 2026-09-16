class Solution:
    """Solver for the longest substring without repeating characters problem."""

    def lengthOfLongestSubstring(self, s: str) -> int:
        """Returns the length of the longest substring without repeating characters.

        Args:
            s: The input string to search.

        Returns:
            The length of the longest substring without repeating characters.
        """
        seen: set[str] = set()
        left: int = 0
        max_length: int = -1

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left)

        return max_length + 1
