class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        
        for s in strs:
            lookup = [0] * 26
            for ch in s:
                lookup[ord('a') - ord(ch)] += 1
            count.setdefault(tuple(lookup), []).append(s)
        
        return list(count.values())
