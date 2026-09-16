class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = defaultdict(list)
        for s in strs:
            lookup = [0] * 26
            for ch in s:
                lookup[ord(ch) - ord('a')] += 1
            freqs[tuple(lookup)].append(s)
        
        return list(freqs.values())
                