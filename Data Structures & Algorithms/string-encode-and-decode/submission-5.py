class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += f"{len(s)}#{s}"
        return enc

    def decode(self, s: str) -> List[str]:
        dec = []
        cursor = 0

        while cursor < len(s):
            start = cursor
            while s[cursor] != "#":
                cursor += 1

            length = int(s[start:cursor])
            cursor += 1  # skip '#'
            dec.append(s[cursor:cursor + length])

            cursor += length

        return dec