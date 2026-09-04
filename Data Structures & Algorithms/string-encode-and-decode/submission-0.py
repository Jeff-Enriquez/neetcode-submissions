class Solution:

    def encode(self, strs: List[str]) -> str:
        str_builder: list[str] = []
        for s in strs:
            str_builder.append(str(len(s)) + "#")
            str_builder.append(s)
        return "".join(str_builder)

    def decode(self, s: str) -> List[str]:
        result: list[str] = []
        i: int = 0
        str_len: int = len(s)
        while i < str_len:
            prefix: str = ""
            while s[i] != "#":
                prefix += s[i]
                i += 1
            i += 1
            end: int = int(prefix)
            result.append(s[i:i + end])
            i += end
        return result

