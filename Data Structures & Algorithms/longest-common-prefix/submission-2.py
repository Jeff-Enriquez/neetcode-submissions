class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c: str = " "
        for col in range(0, len(strs[0])):
            c: str = strs[0][col]
            for row in range(0, len(strs)):
                if col >= len(strs[row]) or c != strs[row][col]:
                    return strs[0][:col]
        return strs[0]