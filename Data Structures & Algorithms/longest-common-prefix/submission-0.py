class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common: list[str] = []
        for col in range(0, len(strs[0])):
            common.append(strs[0][col])
            for row in range(0, len(strs)):
                if col >= len(strs[row]) or common[-1] != strs[row][col]:
                    common.pop()
                    return "".join(common)
        return strs[0]