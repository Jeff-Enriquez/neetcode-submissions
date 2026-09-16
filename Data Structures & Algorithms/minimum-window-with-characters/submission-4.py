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
        s_len: int = len(s)
        t_counts: list[int] = [0] * 58
        s_counts: list[int] = [0] * 58
        for char in t:
            t_counts[ord(char) - ORD_A] += 1
        
        result: tuple[int, int] = (0,0)
        min_len: int = s_len + 1
        left: int = 0
        right: int = 0

        # Find first valid substring
        is_valid_substr: bool = False
        while not is_valid_substr and right < s_len:
            is_valid_substr = True
            s_counts[ord(s[right]) - ORD_A] += 1
            for i in range(58):
                if t_counts[i] > s_counts[i]:
                    is_valid_substr = False
                    break
            right += 1
        
        if not is_valid_substr:
            return ""
        
        min_len = min(min_len, right - left)
        result = (left, right)

        # Sliding window
        while right < s_len:
            left_ord: int = ord(s[left]) - ORD_A
            if t_counts[left_ord] <= s_counts[left_ord] - 1:
                s_counts[left_ord] -= 1
                left += 1
                if right - left < min_len:
                    min_len = right - left
                    result = (left, right)
            else:
                s_counts[ord(s[right]) - ORD_A] += 1
                right += 1
        
        # Final reduction
        left_ord: int = ord(s[left]) - ORD_A
        while t_counts[left_ord] <= s_counts[left_ord] - 1:
            s_counts[left_ord] -= 1
            left += 1
            if right - left < min_len:
                result = (left, right)
            left_ord = ord(s[left]) - ORD_A

        return s[result[0]:result[1]]