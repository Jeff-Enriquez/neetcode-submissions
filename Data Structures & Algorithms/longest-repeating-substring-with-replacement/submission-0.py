class Solution:
    """Solution for the Longest Repeating Character Replacement problem."""

    def characterReplacement(self, s: str, k: int) -> int:
        """Find the length of the longest substring with repeating characters.
        
        Given a string s and an integer k, you can choose any character of the
        string and change it to any other uppercase English character. You can
        perform this operation at most k times.

        Args:
            s: Input string consisting of uppercase English letters.
            k: Maximum number of character replacements allowed.
            
        Returns:
            Length of the longest substring containing the same letter after
            at most k replacements.
        """
        ORD_A = 65  # ASCII value of uppercase 'A' for character index calculation.
        max_len: int = 0
        left: int = 0
        right: int = 0
        counts: list[int] = [0] * 26
        max_count: int = 0

        for right in range(len(s)):
            c_idx: int = ord(s[right]) - ORD_A
            counts[c_idx] += 1
            max_count = max(max_count, counts[c_idx])
            if (right - left + 1) - max_count <= k:
                max_len = max(max_len, right - left + 1)
            else:
                c_idx = ord(s[left]) - ORD_A
                counts[c_idx] -= 1
                if counts[c_idx] + 1 == max_count:
                    for count in counts:
                        max_count = max(max_count, count)
                left += 1

        return max_len
