class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen: set[str] = set()
        l_ptr: int = 0
        longest_string: int = -1
        
        for r_ptr in range(len(s)):
            while s[r_ptr] in seen:
                seen.remove(s[l_ptr])
                l_ptr += 1
            if s[r_ptr] not in seen:
                seen.add(s[r_ptr])
                longest_string = max(longest_string, r_ptr - l_ptr)

        return longest_string + 1
            