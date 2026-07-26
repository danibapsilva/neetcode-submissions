class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = tuple(sorted(s))
            groups.setdefault(key, []).append(s)
        return list(groups.values())
