class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_anagrams: list[list[str]] = []
        group_map: dict[int, list[str]] = {}
        for s in strs:
            char_counts: dict[str, int] = {}
            for c in s:
                char_counts[c] = char_counts.get(c, 0) + 1
            hash_value = Solution.customHash(char_counts)
            group_map.setdefault(hash_value, []).append(s)
        for key, value in group_map.items():
            group_anagrams.append(value)
        return group_anagrams

    def customHash(map: dict[str, int]) -> int:
        hash_sum: int = 0
        for key, value in map.items():
            hash_sum += hash((key, value))
        return hash_sum