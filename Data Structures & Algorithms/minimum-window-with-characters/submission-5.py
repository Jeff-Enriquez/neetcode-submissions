class Solution:
    """Solver for minimum window substring."""

    def minWindow(self, s: str, t: str) -> str:
        """Find minimum window in s containing all characters from t.

        Args:
            s: Source string to search within.
            t: Target string whose characters must all be included.

        Returns:
            The minimum substring of s that contains all characters from t.
            Returns empty string if no such substring exists.
        """
        ORD_A: int = 65
        t_counts: list[int] = [0] * 58
        s_counts: list[int] = [0] * 58
        have: int = 0
        need: int = 0
        for char in t:
            t_counts[ord(char) - ORD_A] += 1
        for count in t_counts:
            if count > 0:
                need += 1
        
        result: tuple[int, int] = (0,-1)
        min_len: int = 100001
        left: int = 0
        for right in range(len(s)):
            right_ord: int = ord(s[right]) - ORD_A
            s_counts[right_ord] += 1
            if s_counts[right_ord] == t_counts[right_ord]:
                have += 1
            
            while have == need:
                if right - left < min_len:
                    min_len = right - left
                    result = (left, right)
                left_ord: int = ord(s[left]) - ORD_A
                s_counts[left_ord] -= 1
                if s_counts[left_ord] < t_counts[left_ord]:
                    have -= 1
                left += 1
    
        return s[result[0]:result[1] + 1]